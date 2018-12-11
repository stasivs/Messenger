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
        MainWindow.resize(749, 759)
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
        self.chat.setObjectName("chat")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.pushMessage = QtWidgets.QPushButton(self.centralwidget)
        self.pushMessage.setGeometry(QtCore.QRect(20, 650, 481, 25))
        self.pushMessage.setObjectName("pushMessage")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 30, 341, 16))
        self.label.setObjectName("label")
        self.Message = QtWidgets.QLineEdit(self.centralwidget)
        self.Message.setGeometry(QtCore.QRect(20, 620, 481, 25))
        self.Message.setObjectName("Message")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(-250, 197, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.IP = QtWidgets.QLineEdit(self.centralwidget)
        self.IP.setGeometry(QtCore.QRect(530, 97, 201, 25))
        self.IP.setObjectName("IP")
        self.IPConnection = QtWidgets.QPushButton(self.centralwidget)
        self.IPConnection.setGeometry(QtCore.QRect(530, 130, 201, 25))
        self.IPConnection.setObjectName("IPConnection")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(530, 60, 341, 51))
        self.label_5.setObjectName("label_5")
        self.Disconnect = QtWidgets.QPushButton(self.centralwidget)
        self.Disconnect.setGeometry(QtCore.QRect(530, 160, 201, 25))
        self.Disconnect.setObjectName("Disconnect")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 749, 21))
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
        self.pushButton_3.setText(_translate("MainWindow", "PushButton"))
        self.IPConnection.setText(_translate("MainWindow", "Подключиться к серверу"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Укажите IP сервера</span></p><p><br/></p></body></html>"))
        self.Disconnect.setText(_translate("MainWindow", "Отключиться от сервера"))

