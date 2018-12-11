from User import *
from Executor import *
from Messages import UserMessage
from Errors import *
from Permissions import *


class Server:
    alreadyBanned = ServerError("IP already banned!")
    notBanned = ServerError("IP has not banned!")
    userNotFound = ServerError("User with nick not found!")

    def __init__(self, ip, port=9090, def_perms=Permissions.Guest):
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
        self.__executor = Executor(self)
        # установка стандартных прав при входе на сервер
        Permissions.Default = def_perms
        self.users.append(ConsoleUser(self))

    def acceptor(self):
        # метод приема новых юзеров (в отдельном потоке)
        while True:
            conn, addr = self.sock.accept()
            u = User(addr[0], conn, self)
            try:
                if u.ip not in self.blacklist:
                    u.accept_success()  # если все ок, добавляем пользователя
                else:
                    u.accept_canceled(User.youBannedMessage)  # если забанен, то отменяем вход
            except ServerError as se:
                print("Error:", se.get_text())

    def resend(self, message):
        # ретрансляция сообщений всем юзерам
        for u in self.users:
            try:
                u.send(message)
            except ServerError as se:
                print("Error:", se.get_text())

    def manager(self, message, owner):
        # распределние приходящей информации на команды или сообщения юзера
        if len(message.get_message()) == 0:
            return
        if message.get_message()[0] == "/":
            name = message.text[1:].split()[0]
            args = message.text[1:].split()[1:]
            self.__executor.execute(name, args, owner)  # отправка в обработчик команд
        else:
            # формирование нормального вида сообщения пользователя и отправка остальным
            message = UserMessage(message.get_message(), owner.nick)
            self.resend(message)

    def get_user_by_nick(self, nick):
        # получение объекта юзера по нику
        for u in self.users:
            if u.nick == nick:
                return u
        raise Server.userNotFound

    def ban(self, ip):
        # блокировка ip адреса
        if ip in self.blacklist:
            raise Server.alreadyBanned
        self.blacklist.append(ip)

    def unban(self, ip):
        # разблокировка ip адреса
        if ip not in self.blacklist:
            raise Server.notBanned
        self.blacklist.remove(ip)


if __name__ == "__main__":
    ip = input("IP: ")
    server = Server(ip, 9090, Permissions.Guest)
