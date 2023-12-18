# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.accountButton = QtWidgets.QPushButton(self.centralwidget)
        self.accountButton.setGeometry(QtCore.QRect(50, 20, 89, 25))
        self.accountButton.setObjectName("accountButton")
        self.statementButton = QtWidgets.QPushButton(self.centralwidget)
        self.statementButton.setGeometry(QtCore.QRect(210, 20, 131, 25))
        self.statementButton.setObjectName("statementButton")
        self.transactionButton = QtWidgets.QPushButton(self.centralwidget)
        self.transactionButton.setGeometry(QtCore.QRect(420, 20, 141, 25))
        self.transactionButton.setObjectName("transactionButton")
        self.signoutButton = QtWidgets.QPushButton(self.centralwidget)
        self.signoutButton.setGeometry(QtCore.QRect(640, 20, 89, 25))
        self.signoutButton.setObjectName("signoutButton")
        self.phoneLabel = QtWidgets.QLabel(self.centralwidget)
        self.phoneLabel.setGeometry(QtCore.QRect(70, 160, 151, 20))
        self.phoneLabel.setObjectName("phoneLabel")
        self.moneyLabel = QtWidgets.QLabel(self.centralwidget)
        self.moneyLabel.setGeometry(QtCore.QRect(350, 160, 67, 17))
        self.moneyLabel.setObjectName("moneyLabel")
        self.operationLabel = QtWidgets.QLabel(self.centralwidget)
        self.operationLabel.setGeometry(QtCore.QRect(570, 160, 81, 17))
        self.operationLabel.setObjectName("operationLabel")
        self.sendPhone = QtWidgets.QLineEdit(self.centralwidget)
        self.sendPhone.setGeometry(QtCore.QRect(70, 220, 151, 25))
        self.sendPhone.setObjectName("sendPhone")
        self.requestPhone = QtWidgets.QLineEdit(self.centralwidget)
        self.requestPhone.setGeometry(QtCore.QRect(70, 290, 151, 25))
        self.requestPhone.setObjectName("requestPhone")
        self.sendMoney = QtWidgets.QLineEdit(self.centralwidget)
        self.sendMoney.setGeometry(QtCore.QRect(320, 220, 113, 25))
        self.sendMoney.setObjectName("sendMoney")
        self.requestMoney = QtWidgets.QLineEdit(self.centralwidget)
        self.requestMoney.setGeometry(QtCore.QRect(320, 290, 113, 25))
        self.requestMoney.setObjectName("requestMoney")
        self.sendButton = QtWidgets.QPushButton(self.centralwidget)
        self.sendButton.setGeometry(QtCore.QRect(550, 220, 111, 25))
        self.sendButton.setObjectName("sendButton")
        self.requestButton = QtWidgets.QPushButton(self.centralwidget)
        self.requestButton.setGeometry(QtCore.QRect(550, 290, 111, 25))
        self.requestButton.setObjectName("requestButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 80, 67, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(400, 80, 67, 17))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 28))
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
        self.accountButton.setText(_translate("MainWindow", "Account"))
        self.statementButton.setText(_translate("MainWindow", "Check Statements"))
        self.transactionButton.setText(_translate("MainWindow", "Seach Transactions"))
        self.signoutButton.setText(_translate("MainWindow", "Sign Out"))
        self.phoneLabel.setText(_translate("MainWindow", "Phone number/Email"))
        self.moneyLabel.setText(_translate("MainWindow", "Money"))
        self.operationLabel.setText(_translate("MainWindow", "Operation"))
        self.sendButton.setText(_translate("MainWindow", "Send Money"))
        self.requestButton.setText(_translate("MainWindow", "Request Money"))
        self.label.setText(_translate("MainWindow", "Hello!"))
        self.label_2.setText(_translate("MainWindow", "User"))


class MainMenu(Ui_MainWindow):
    def __init__(self, username, db_conn):
        super(MainMenu, self).__init__()
        self.mainwindow=QMainWindow()
        self.setupUi(self.mainwindow)
        self.label_2.setText(username)
        self.conn = db_conn
        # 绑定按钮点击后调用的函数
        self.sendButton.clicked.connect(self.sendMoneyFun)
        self.requestButton.clicked.connect(self.requestMoneyFun)

    # 在下面编写按钮点击处理逻辑
    def sendMoneyFun(self):
        # 获取文本输入框的值 输入文本框是QLineEdit对象
        people = self.sendPhone.text()
        money = self.sendMoney.text()
        print(people)
        print(money)
        # 读取数据, call conn.commit() if make any changes to the database
        cursor = self.conn.cursor()
        # cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

        # conn.commit()  # 如果是写数据库的话记得调用这个
        print("sendMoney")


    def requestMoneyFun(self):

        print("requestMoney")