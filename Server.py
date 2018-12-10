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
        if message.text[0] == "/":
            name = message.text[1:].split()[0]
            args = message.text[1:].split()[1:]
            self.executor.execute(name, args, owner)  # отправка в обработчик команд
        else:
            # формирование нормального вида сообщения пользователя и отправка остальным
            message = UserMessage(message.get_message(), owner.nick)
            self.resend(message)
