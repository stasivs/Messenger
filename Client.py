import sys
import pickle
from PyQt5.QtWidgets import QApplication, QMainWindow
from UI import Ui_MainWindow
import Messages
import Server
import socket

'''
Объекты :
pushMessage - Кнопка отправки введенного в поле Message
Message - Поле для набора сообщения
setNickname - Кнопка смены никнейма на тот, что указан в поле Nickname
Nickname - Поле для набора никнейма 
chat - Чат
IP - Поле для набора айпи
Port - Поле для набора порта
PortConnection - Кнопка для подключения к указанному IP с указанным PORT

Массивы :
Добавил массив сообщений и его наполнение
'''


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.main()
        self.sock = None

    def main(self):
        self.pushMessage.clicked.connect(self.sendMessage)
        self.setNickname.clicked.connect(self.changeNickname)
        self.PortConnection.clicked.connect(self.connect)

    def showMessage(self, message):
        self.chat.append(message.get_text())

    def receiveMessage(self):
        while True:
            message = pickle.loads(self.sock.recv(1024))
            if message is None:
                continue
            self.showMessage(message)

    def sendMessage(self):
        message = Messages.BlankMessage(self.Message.text())
        self.sock.send(pickle.dumps(message))

    def changeNickname(self):
        pass

    def connect(self):
        ip, port = self.IP.text(), 9090
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.sock.connect((ip, port))
        except Exception:
            print("Ошибка")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
