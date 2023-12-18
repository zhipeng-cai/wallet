# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'searchwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow


class Ui_SearchWindow(object):
    def setupUi(self, SearchWindow):
        SearchWindow.setObjectName("SearchWindow")
        SearchWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(SearchWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.helloLabel = QtWidgets.QLabel(self.centralwidget)
        self.helloLabel.setGeometry(QtCore.QRect(280, 40, 67, 17))
        self.helloLabel.setObjectName("helloLabel")
        self.usernameLabel = QtWidgets.QLabel(self.centralwidget)
        self.usernameLabel.setGeometry(QtCore.QRect(380, 40, 91, 17))
        self.usernameLabel.setObjectName("usernameLabel")
        self.ssnLabel = QtWidgets.QLabel(self.centralwidget)
        self.ssnLabel.setGeometry(QtCore.QRect(110, 160, 67, 17))
        self.ssnLabel.setObjectName("ssnLabel")
        self.ssn_input = QtWidgets.QLineEdit(self.centralwidget)
        self.ssn_input.setGeometry(QtCore.QRect(240, 160, 171, 25))
        self.ssn_input.setObjectName("ssn_input")
        self.emailLabel = QtWidgets.QLabel(self.centralwidget)
        self.emailLabel.setGeometry(QtCore.QRect(110, 230, 111, 17))
        self.emailLabel.setObjectName("emailLabel")
        self.guidelabel = QtWidgets.QLabel(self.centralwidget)
        self.guidelabel.setGeometry(QtCore.QRect(190, 100, 381, 17))
        self.guidelabel.setObjectName("guidelabel")
        self.email_input = QtWidgets.QLineEdit(self.centralwidget)
        self.email_input.setGeometry(QtCore.QRect(240, 226, 171, 25))
        self.email_input.setObjectName("email_input")
        self.phoneLabel = QtWidgets.QLabel(self.centralwidget)
        self.phoneLabel.setGeometry(QtCore.QRect(110, 300, 111, 17))
        self.phoneLabel.setObjectName("phoneLabel")
        self.phone_input = QtWidgets.QLineEdit(self.centralwidget)
        self.phone_input.setGeometry(QtCore.QRect(240, 292, 171, 25))
        self.phone_input.setObjectName("phone_input")
        self.transactionLabel = QtWidgets.QLabel(self.centralwidget)
        self.transactionLabel.setGeometry(QtCore.QRect(110, 370, 121, 17))
        self.transactionLabel.setObjectName("transactionLabel")
        self.transactio_input = QtWidgets.QComboBox(self.centralwidget)
        self.transactio_input.setGeometry(QtCore.QRect(240, 368, 171, 25))
        self.transactio_input.setObjectName("transactio_input")
        self.dateLabel = QtWidgets.QLabel(self.centralwidget)
        self.dateLabel.setGeometry(QtCore.QRect(110, 440, 121, 17))
        self.dateLabel.setObjectName("dateLabel")
        self.startDate = QtWidgets.QDateEdit(self.centralwidget)
        self.startDate.setGeometry(QtCore.QRect(240, 440, 81, 26))
        self.startDate.setObjectName("startDate")
        self.endDate = QtWidgets.QDateEdit(self.centralwidget)
        self.endDate.setGeometry(QtCore.QRect(340, 440, 81, 26))
        self.endDate.setObjectName("endDate")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(328, 443, 15, 17))
        self.label_9.setObjectName("label_9")
        self.searchButton = QtWidgets.QPushButton(self.centralwidget)
        self.searchButton.setGeometry(QtCore.QRect(520, 270, 89, 41))
        self.searchButton.setObjectName("searchButton")
        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setGeometry(QtCore.QRect(720, 510, 61, 25))
        self.backButton.setObjectName("backButton")
        SearchWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SearchWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 28))
        self.menubar.setObjectName("menubar")
        SearchWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SearchWindow)
        self.statusbar.setObjectName("statusbar")
        SearchWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SearchWindow)
        QtCore.QMetaObject.connectSlotsByName(SearchWindow)

    def retranslateUi(self, SearchWindow):
        _translate = QtCore.QCoreApplication.translate
        SearchWindow.setWindowTitle(_translate("SearchWindow", "MainWindow"))
        self.helloLabel.setText(_translate("SearchWindow", "Hello!"))
        self.usernameLabel.setText(_translate("SearchWindow", "v_username"))
        self.ssnLabel.setText(_translate("SearchWindow", "SSN:"))
        self.emailLabel.setText(_translate("SearchWindow", "Email Address:"))
        self.guidelabel.setText(_translate("SearchWindow", "You can search the transactions by the following keys."))
        self.phoneLabel.setText(_translate("SearchWindow", "Phone Number:"))
        self.transactionLabel.setText(_translate("SearchWindow", "Transaction Type:"))
        self.dateLabel.setText(_translate("SearchWindow", "Date Range:"))
        self.label_9.setText(_translate("SearchWindow", "~"))
        self.searchButton.setText(_translate("SearchWindow", "Search"))
        self.backButton.setText(_translate("SearchWindow", "Back"))
        # Add options to the combo box
        self.transactio_input.addItem("Send")
        self.transactio_input.addItem("Request")


class SearchMenu(Ui_SearchWindow):
    def __init__(self, username, db_conn):
        super(SearchMenu, self).__init__()
        self.searchwindow=QMainWindow()
        self.setupUi(self.searchwindow)
        self.usernameLabel.setText(username)
        self.conn = db_conn
        # 绑定按钮点击后调用的函数
        self.searchButton.clicked.connect(self.searchFun)


    def searchFun(self):
        # 根据各个文本框的数据作为限制条件来查询
        # 可能要学习一下怎么读取QDateEdit对象的日期数据
        print("searchFun")