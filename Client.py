import sys
import pickle
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt
from UI import Ui_MainWindow
import Messages
import threading
import socket

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
        self.connected = False

    def main(self):
        self.pushMessage.clicked.connect(self.sendMessage)
        self.IPConnection.clicked.connect(self.connect)
        self.Disconnect.clicked.connect(self.disconect)

    def showMessage(self, message):
        self.chat.append(message.get_message())

    def receiveMessage(self):
        while self.connected:
            message = pickle.loads(self.sock.recv(1024))
            if message is None:
                continue
            self.showMessage(message)

    def keyPressEvent(self, event):
        if event.key() + 1 == Qt.Key_Enter:
            self.sendMessage()

    def sendMessage(self):
        if self.connected:
            message = Messages.BlankMessage(self.Message.text())
            self.sock.send(pickle.dumps(message))
            self.Message.setText("")
        else:
            self.chat.append("Вы не подключились к серверу")

    def connect(self):
        ip = self.IP.text()
        self.connected = True
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

    def disconnect(self):
        if self.connected:
            self.connected = False
            self.sock.close()
            self.setWindowTitle("Чат")
            self.chat.append("Вы покинули сервер!")
        else:
            self.chat.append("Чтобы откуда-то выйти надо туда зайти")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
