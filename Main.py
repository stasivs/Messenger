import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from UI import Ui_MainWindow

'''
Объекты :
pushMessage - Кнопка отправки введенного в поле Message
Message - Поле для набора сообщения
setNickname - Кнопка смены никнейма на тот, что указан в поле Nickname
Nickname - Поле для набора никнейма 
chat - Чат
Port - Поле для набора порта
PortCreation - Кнопка для создания сервера с указанным в поле Port портом
PortConnection - Кнопка для подключения к указанному в поле Port порту

Массивы :
Добавил массив сообщений и его наполнение
'''



class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.nick = "Неопознанный арбуз"
        self.MAXLEN = 55
        self.main()
        self.messages = []

    def main(self):
        self.pushMessage.clicked.connect(self.writeMessage)
        self.setNickname.clicked.connect(self.changeNickname)

    def writeMessage(self):
        startmessage = len(self.nick) + 2
        temp = self.Message.text()
        self.chat.addItem(self.nick + ": " + self.Message.text()[: self.MAXLEN - startmessage])
        for i in range(1, len(temp) // self.MAXLEN + 1):
            self.chat.addItem(temp[startmessage + (i - 1) * self.MAXLEN: i * self.MAXLEN])
        self.Message.setText("")
        self.messages.append(temp)

    def changeNickname(self):
        temp = self.Nickname.text().strip()
        if temp == "":
            print("Нельзя сменить имя")
        elif len(temp) > 20:
            print("Слишком длинное имя")
        else:
            oldNick = self.nick
            self.nick = temp
            self.chat.addItem("{} сменил имя на {}".format(oldNick, self.nick))
            self.showNick.setText(self.nick)
        self.Nickname.setText("")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
