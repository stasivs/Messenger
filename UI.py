# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(788, 759)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(20, 60, 481, 551))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 479, 549))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.chat = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        self.chat.setGeometry(QtCore.QRect(0, 0, 481, 551))
        self.chat.setObjectName("textBrowser")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.pushMessage = QtWidgets.QPushButton(self.centralwidget)
        self.pushMessage.setGeometry(QtCore.QRect(20, 667, 481, 25))
        self.pushMessage.setObjectName("pushMessage")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 30, 341, 16))
        self.label.setObjectName("label")
        self.Message = QtWidgets.QLineEdit(self.centralwidget)
        self.Message.setGeometry(QtCore.QRect(20, 627, 481, 25))
        self.Message.setObjectName("Message")
        self.setNickname = QtWidgets.QPushButton(self.centralwidget)
        self.setNickname.setGeometry(QtCore.QRect(520, 257, 201, 25))
        self.setNickname.setObjectName("setNickname")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(520, 70, 341, 16))
        self.label_2.setObjectName("label_2")
        self.showNick = QtWidgets.QLabel(self.centralwidget)
        self.showNick.setGeometry(QtCore.QRect(520, 120, 341, 21))
        self.showNick.setObjectName("showNick")
        self.Nickname = QtWidgets.QLineEdit(self.centralwidget)
        self.Nickname.setGeometry(QtCore.QRect(520, 207, 201, 25))
        self.Nickname.setObjectName("Nickname")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(520, 170, 411, 16))
        self.label_4.setObjectName("label_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(-250, 197, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.PortConnection = QtWidgets.QPushButton(self.centralwidget)
        self.PortConnection.setGeometry(QtCore.QRect(520, 437, 201, 25))
        self.PortConnection.setObjectName("PortConnection")
        self.IP = QtWidgets.QLineEdit(self.centralwidget)
        self.IP.setGeometry(QtCore.QRect(520, 397, 201, 25))
        self.IP.setObjectName("IP")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(520, 340, 341, 51))
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 788, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushMessage.setText(_translate("MainWindow", "Отправить"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">                                         ЧАТ</span></p></body></html>"))
        self.setNickname.setText(_translate("MainWindow", "Сменить"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Ваш никнейм :</span></p></body></html>"))
        self.showNick.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Неопознанный арбуз</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Изменить никнейм :</span></p></body></html>"))
        self.pushButton_3.setText(_translate("MainWindow", "PushButton"))
        self.PortConnection.setText(_translate("MainWindow", "Подключиться к серверу"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Укажите айпи сервера</span></p></body></html>"))

