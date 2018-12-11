import threading
from Errors import *
from Messages import *
from Permissions import *
import pickle
import socket


class User:
    # класс, описывающий одного юзера

    count = 0

    # сообщения для пользователей
    youBannedMessage = Error("You have banned on this server!")

    # внутренние ошибки
    notOnServer = ServerError("User not on server!")
    alreadyOnServer = ServerError("User already on server!")

    def __init__(self, ip, conn, server):
        # установка адреса, соединения, ника, потока приема
        self.ip = ip
        self.__conn = conn
        self.nick = "Guest#" + str(User.count)
        self.__th = threading.Thread(target=self.receive, daemon=True)
        # установка переменной состояния и принадлежности к серверу
        self.__onServer = False
        self.server = server
        self.permissions = Permissions.Guest  # права

    def accept_success(self):
        # метод для обработки успешного входа на сервер
        if self.__onServer:
            raise User.alreadyOnServer
        self.send(Info("Connect success! Welcome on IP: {}".format(
            self.server.HOST
        )))
        self.server.resend(Bcast("Connected {} ({})".format(
            self.nick,
            self.ip
        )))
        self.server.users.append(self)
        User.count += 1  # увеличения статической переменной кол-ва юзеров
        self.__onServer = True  # переменная состояния в положение <на сервере>
        self.permissions = Permissions.Default  # выдаем права пользователя
        self.__th.start()  # включаем поток обработки приходящих сообщений

    def accept_canceled(self, reason):
        # метод для обработки неуспешного входа на сервер
        if not self.__onServer:
            raise User.notOnServer
        self.send(Info("Connect canceled, because: {}".format(
            reason
        )))
        self.disconnect()

    def disconnect(self, reason="*not_defined*"):
        # метод для обработки отключения от сервера
        if not self.__onServer:
            raise User.notOnServer
        if self in self.server.users:
            self.server.users.remove(self)
        self.__onServer = False
        self.send(Info("You disconnected, because: {}".format(
            reason
        )))
        self.__conn.close()
        self.server.resend(Bcast("Disconnected {} ({})".format(
            self.nick,
            self.ip
        )))

    def send(self, message):
        # отправка сообщения этому пользователю
        data = pickle.dumps(message)
        try:
            self.__conn.send(data)
        except ConnectionResetError:
            if self.__onServer:
                self.disconnect()
                raise User.notOnServer

    def receive(self):
        # прием сообщения от этого пользователя (в отдельном потоке)
        while self.__onServer:
            try:
                data = self.__conn.recv(1024)
            except socket.error:
                self.disconnect()
                return
            except ConnectionResetError:
                self.disconnect()
                return
            if not data:
                continue
            # десериализация сообщения и передача в обработчик сообщений сервера
            message = pickle.loads(data)
            self.server.manager(message, self)


class ConsoleUser (User):
    # Создание супер-пользователя (консоль сервера)

    def __init__(self, server):
        # убираем переменныу conn и ip, так как консоль не явлется удаленной
        self.nick = "*console*"
        self.__onServer = True
        self.server = server
        self.permissions = Permissions.Console  # права
        self.receive()

    # переопределяем методы приема/отправки под консоль
    def send(self, message):
        if isinstance(message, UserMessage):
            return
        print(message.get_message())

    def receive(self):
        while True:
            message = BlankMessage(input())
            self.server.manager(message, self)

    # убираем ненужные для консоли методы
    def accept_canceled(self, reason):
        pass

    def accept_success(self):
        pass

    def disconnect(self, reason="*not_defined*"):
        pass
