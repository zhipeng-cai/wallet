# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Welcome")
        Form.resize(400, 300)
        self.usernameLabel = QtWidgets.QLabel(Form)
        self.usernameLabel.setGeometry(QtCore.QRect(90, 90, 71, 21))
        self.usernameLabel.setObjectName("usernameLabel")
        self.passwordLabel = QtWidgets.QLabel(Form)
        self.passwordLabel.setGeometry(QtCore.QRect(90, 130, 67, 17))
        self.passwordLabel.setObjectName("passwordLabel")
        self.usernameInput = QtWidgets.QLineEdit(Form)
        self.usernameInput.setGeometry(QtCore.QRect(180, 90, 113, 25))
        self.usernameInput.setObjectName("usernameInput")
        self.passwordInput = QtWidgets.QLineEdit(Form)
        self.passwordInput.setGeometry(QtCore.QRect(180, 130, 113, 25))
        self.passwordInput.setObjectName("passwordInput")
        self.loginButton = QtWidgets.QPushButton(Form)
        self.loginButton.setGeometry(QtCore.QRect(200, 190, 89, 25))
        self.loginButton.setObjectName("loginButton")
        self.signupButton = QtWidgets.QPushButton(Form)
        self.signupButton.setGeometry(QtCore.QRect(90, 190, 89, 25))
        self.signupButton.setObjectName("signupButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.usernameLabel.setText(_translate("Form", "Username"))
        self.passwordLabel.setText(_translate("Form", "Password"))
        self.loginButton.setText(_translate("Form", "Log In"))
        self.signupButton.setText(_translate("Form", "Sign Up"))



class LoginMenu(Ui_Form):
    def __init__(self,window):
        super(LoginMenu, self).__init__()
        self.loginwindow=QMainWindow()
        self.setupUi(self.loginwindow)
        self.center_window()

    def center_window(self):
        desktop = QDesktopWidget()

        screen_rect = desktop.screenGeometry()
        x = (screen_rect.width() - self.loginwindow.width()) // 2
        y = (screen_rect.height() - self.loginwindow.height()) // 2

        self.loginwindow.move(x, y)