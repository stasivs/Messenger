import sys
import pickle
from PyQt5.QtWidgets import QApplication, QMainWindow
from UI import Ui_MainWindow
import Messages
import threading
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

wrongAddr = Messages.Error("Wrong server adress!")
failedServer = Messages.Error("Failed connect to server!")


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.main()
        self.th = threading.Thread(target=self.receiveMessage)
        self.th.daemon = True
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def main(self):
        self.pushMessage.clicked.connect(self.sendMessage)
        self.setNickname.clicked.connect(self.changeNickname)
        self.PortConnection.clicked.connect(self.connect)

    def showMessage(self, message):
        self.chat.append(message.get_message())

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
        ip = self.IP.text()
        try:
            self.sock.connect((ip, 9090))
        except socket.gaierror:
            self.showMessage(wrongAddr)
            return
        except OSError:
            self.showMessage(failedServer)
            return
        self.th.start()
        self.setWindowTitle("Connected to " + ip)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
