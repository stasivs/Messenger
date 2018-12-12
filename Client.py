import sys
import pickle
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt
from UI import Ui_MainWindow
import Messages
import threading
import socket

wrongAddr = Messages.Error("Wrong server address!")
failedServer = Messages.Error("Failed connect to server!")
notConnected = Messages.Error("You have not connected!")
youDisconnected = Messages.Info("You disconnected from server!")
alreadyConnected = Messages.Error("You already connected")


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.main()
        self.th = None
        self.sock = None
        self.connected = False

    def main(self):
        self.pushMessage.clicked.connect(self.sendMessage)
        self.IPConnection.clicked.connect(self.connect)
        self.Disconnect.clicked.connect(self.disconnect)

    def showMessage(self, message):
        self.chat.append(message.get_message())

    def receiveMessage(self):
        while self.connected:
            try:
                message = pickle.loads(self.sock.recv(1024))
            except Exception:
                return
            if message is None:
                continue
            self.showMessage(message)

    def keyPressEvent(self, event):
        if event.key() + 1 == Qt.Key_Enter and self.connected:
            self.sendMessage()

    def sendMessage(self):
        if self.connected:
            message = Messages.BlankMessage(self.Message.text())
            self.sock.send(pickle.dumps(message))
            self.Message.setText("")
        else:
            self.showMessage(notConnected)

    def connect(self):
        if self.connected:
            self.showMessage(alreadyConnected)
            return
        ip = self.IP.text()
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect((ip, 9090))
        except socket.gaierror:
            self.showMessage(wrongAddr)
            return
        except OSError:
            self.showMessage(failedServer)
            return
        self.connected = True
        self.th = threading.Thread(target=self.receiveMessage)
        self.th.daemon = True
        self.th.start()
        self.setWindowTitle("Connected to " + ip)

    def disconnect(self):
        if self.connected:
            self.connected = False
            self.sock.close()
            self.setWindowTitle("Local Network Messenger")
            self.showMessage(youDisconnected)
        else:
            self.showMessage(notConnected)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
