# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'statementwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow


class Ui_StatementWindow(object):
    def setupUi(self, StatementWindow):
        StatementWindow.setObjectName("StatementWindow")
        StatementWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(StatementWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.helloLabel = QtWidgets.QLabel(self.centralwidget)
        self.helloLabel.setGeometry(QtCore.QRect(270, 50, 67, 17))
        self.helloLabel.setObjectName("helloLabel")
        self.usernameLabel = QtWidgets.QLabel(self.centralwidget)
        self.usernameLabel.setGeometry(QtCore.QRect(380, 50, 91, 17))
        self.usernameLabel.setObjectName("usernameLabel")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(80, 100, 521, 17))
        self.label_3.setObjectName("label_3")
        self.startDate = QtWidgets.QDateEdit(self.centralwidget)
        self.startDate.setGeometry(QtCore.QRect(80, 130, 91, 26))
        self.startDate.setObjectName("startDate")
        self.endDate = QtWidgets.QDateEdit(self.centralwidget)
        self.endDate.setGeometry(QtCore.QRect(190, 130, 91, 26))
        self.endDate.setObjectName("endDate")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(175, 132, 15, 17))
        self.label_4.setObjectName("label_4")
        self.answer1 = QtWidgets.QLabel(self.centralwidget)
        self.answer1.setGeometry(QtCore.QRect(340, 133, 331, 17))
        self.answer1.setObjectName("answer1")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(80, 190, 521, 17))
        self.label_6.setObjectName("label_6")
        self.answer2List = QtWidgets.QListWidget(self.centralwidget)
        self.answer2List.setGeometry(QtCore.QRect(80, 220, 461, 71))
        self.answer2List.setObjectName("answer2List")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(80, 330, 521, 17))
        self.label_7.setObjectName("label_7")
        self.answer3 = QtWidgets.QLabel(self.centralwidget)
        self.answer3.setGeometry(QtCore.QRect(80, 360, 521, 17))
        self.answer3.setObjectName("answer3")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(80, 410, 601, 17))
        self.label_9.setObjectName("label_9")
        self.answer4 = QtWidgets.QLabel(self.centralwidget)
        self.answer4.setGeometry(QtCore.QRect(80, 440, 521, 17))
        self.answer4.setObjectName("answer4")
        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setGeometry(QtCore.QRect(730, 520, 61, 25))
        self.backButton.setObjectName("backButton")
        StatementWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(StatementWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 28))
        self.menubar.setObjectName("menubar")
        StatementWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(StatementWindow)
        self.statusbar.setObjectName("statusbar")
        StatementWindow.setStatusBar(self.statusbar)

        self.retranslateUi(StatementWindow)
        QtCore.QMetaObject.connectSlotsByName(StatementWindow)

    def retranslateUi(self, StatementWindow):
        _translate = QtCore.QCoreApplication.translate
        StatementWindow.setWindowTitle(_translate("StatementWindow", "MainWindow"))
        self.helloLabel.setText(_translate("StatementWindow", "Hello!"))
        self.usernameLabel.setText(_translate("StatementWindow", "v_username"))
        self.label_3.setText(_translate("StatementWindow", "1. Total amount of money sent/received by a user in a range of dates:"))
        self.label_4.setText(_translate("StatementWindow", "~"))
        self.answer1.setText(_translate("StatementWindow", "no result"))
        self.label_6.setText(_translate("StatementWindow", "2. Total amount of money sent and received by a user per month:"))
        self.label_7.setText(_translate("StatementWindow", "3. The transactions with the maximum amount of money per month:"))
        self.answer3.setText(_translate("StatementWindow", "no result"))
        self.label_9.setText(_translate("StatementWindow", "4. The best users (users who have sent/received the maximum total amount of money):"))
        self.answer4.setText(_translate("StatementWindow", "no result"))
        self.backButton.setText(_translate("StatementWindow", "Back"))


class StatementMenu(Ui_StatementWindow):
    def __init__(self, username):
        super(StatementMenu, self).__init__()
        self.statementwindow=QMainWindow()
        self.setupUi(self.statementwindow)
        self.usernameLabel.setText(username)