import threading
from Messages import *
import pickle
import socket


class User:
    # класс, описывающий одного юзера

    count = 0

    notOnServer = Error("User not on server!")
    userNotFound = Error("User with this nick not found!")
    youBanned = Info("You have banned on this server!")
    alreadyBanned = Error("This ip already banned!")
    notBanned = Error("This ip has not banned!")

    def __init__(self, ip, conn, server):
        # установка адреса, соединения, ника, потока приема
        self.ip = ip
        self.__conn = conn
        self.nick = "Guest#" + str(User.count)
        self.__th = threading.Thread(target=self.receive, daemon=True)
        # установка переменной состояния и принадлежности к серверу
        self.__onServer = False
        self.server = server

    def accept_success(self):
        # метод для обработки успешного входа на сервер
        if self.__onServer:
            return
        self.send(Info("Connect success! Welcome on IP: ") + self.server.HOST)
        self.server.resend(Bcast("Connected {} ({})".format(
            self.nick,
            self.ip
        )))
        self.server.users.append(self)
        User.count += 1  # увеличения статической переменной кол-ва юзеров
        self.__onServer = True  # переменная состояния в положение <на сервере>
        self.__th.start()  # включаем поток обработки приходящих сообщений

    def accept_canceled(self, reason):
        # метод для обработки неуспешного входа на сервер
        if not self.__onServer:
            return
        self.send(Info("Connect canceled, because: {}".format(
            reason
        )))
        self.disconnect()

    def disconnect(self, reason="*not_defined*"):
        # метод для обработки отключения от сервера
        if not self.__onServer:
            return User.notOnServer
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
                return User.notOnServer

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
