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

    def main(self):
        self.pushMessage.clicked.connect(self.showMessage)
        self.setNickname.clicked.connect(self.changeNickname)
        self.PortConnection.clicked.connect(self.connect)

    def showMessage(self, message):
        self.chat.append(self.receiveMessage(message))

    def receiveMessage(self, message):
        return pickle.loads(message)

    def sendMessage(self):
        message = Messages.UserMessage(self.Message.text())

    def changeNickname(self):
        pass

    def connect(self):
        ip, port = self.IP.text(), 9090
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sock.connect((ip, port))
        except Exception:
            print("Ошибка")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
