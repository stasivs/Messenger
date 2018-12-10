import socket
import threading
from User import User
from Messages import *
from Executor import *


class Server:
    def __init__(self, ip, port=9090):
        # установка адреса, порта, главного сокета
        self.HOST = ip
        self.PORT = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.HOST, self.PORT))
        self.sock.listen(10)
        # инициализация списков юзеров, блокировок
        self.blacklist = []
        self.users = []
        # создание потока приема новых пользователей
        self.th = threading.Thread(target=self.acceptor)
        self.th.start()
        # создание обработчика команд
        self.executor = Executor(self)

    def acceptor(self):
        # метод приема новых юзеров (в отдельном потоке)
        while True:
            conn, addr = self.sock.accept()
            u = User(addr[0], conn, self)
            if u.ip not in self.blacklist:
                u.accept_success()  # если все ок, добавляем пользователя
            else:
                u.accept_canceled(User.youBanned)  # если забанен, то отменяем вход

    def resend(self, message):
        # ретрансляция сообщений всем юзерам
        for u in self.users:
            u.send(message)

    def manager(self, message, owner):
        # распределние приходящей информации на команды или сообщения юзера
        if message.get_text()[0] == "/":
            name = message.text[1:].split()[0]
            args = message.text[1:].split()[1:]
            self.executor.execute(name, args, owner)  # отправка в обработчик команд
        else:
            # формирование нормального вида сообщения пользователя и отправка остальным
            message = UserMessage(message.get_message(), owner.nick)
            self.resend(message)

    def get_user_by_nick(self, nick):
        # получение объекта юзера по нику
        for u in self.users:
            if u.nick == nick:
                return u
        return User.userNotFound

    def ban(self, ip):
        # блокировка ip адреса
        if ip in self.blacklist:
            return User.alreadyBanned
        self.blacklist.append(ip)

    def unban(self, ip):
        # разблокировка ip адреса
        if ip not in self.blacklist:
            return User.notBanned
        self.blacklist.remove(ip)

