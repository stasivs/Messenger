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
        MainWindow.resize(775, 759)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(20, 60, 481, 551))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 479, 549))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.chat = QtWidgets.QListWidget(self.scrollAreaWidgetContents)
        self.chat.setGeometry(QtCore.QRect(0, 0, 481, 551))
        self.chat.setObjectName("chat")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.pushMessage = QtWidgets.QPushButton(self.centralwidget)
        self.pushMessage.setGeometry(QtCore.QRect(20, 667, 481, 25))
        self.pushMessage.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 30, 341, 16))
        self.label.setObjectName("label")
        self.Message = QtWidgets.QLineEdit(self.centralwidget)
        self.Message.setGeometry(QtCore.QRect(20, 630, 481, 23))
        self.Message.setObjectName("Message")
        self.setNickname = QtWidgets.QPushButton(self.centralwidget)
        self.setNickname.setGeometry(QtCore.QRect(550, 267, 201, 25))
        self.setNickname.setObjectName("setNickname")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(550, 70, 341, 16))
        self.label_2.setObjectName("label_2")
        self.showNick = QtWidgets.QLabel(self.centralwidget)
        self.showNick.setGeometry(QtCore.QRect(550, 120, 341, 16))
        self.showNick.setObjectName("showNick")
        self.Nickname = QtWidgets.QLineEdit(self.centralwidget)
        self.Nickname.setGeometry(QtCore.QRect(550, 230, 201, 23))
        self.Nickname.setObjectName("Nickname")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(550, 190, 411, 16))
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 775, 21))
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
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">ЧАТ</span></p></body></html>"))
        self.setNickname.setText(_translate("MainWindow", "Сменить"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Ваш никнейм :</span></p></body></html>"))
        self.showNick.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:8pt;\">Неопознанный арбуз</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Изменить никнейм :</span></p></body></html>"))

