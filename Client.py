import sys
import pickle
from PyQt5.QtWidgets import QApplication, QMainWindow
from UI import Ui_MainWindow
import Messages
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
        self.pushMessage.clicked.connect(self.writeMessage)
        self.setNickname.clicked.connect(self.changeNickname)
        self.PortConnection.clicked.connect(self.connect)

    def writeMessage(self):
        self.chat.append("TEXT")

    def sendMessage(self):
        message = Messages.UserMessage(self.Message.text())

    def changeNickname(self):
        pass

    def connect(self):
        ip, port = self.IP.text(), self.Port.text()
        print(ip, port)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
