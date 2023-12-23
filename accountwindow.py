# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'accountwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow


class Ui_AccountWindow(object):
    def setupUi(self, AccountWindow):
        AccountWindow.setObjectName("AccountWindow")
        AccountWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(AccountWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.usernameLabel = QtWidgets.QLabel(self.centralwidget)
        self.usernameLabel.setGeometry(QtCore.QRect(70, 60, 71, 17))
        self.usernameLabel.setObjectName("usernameLabel")
        self.v_username = QtWidgets.QLabel(self.centralwidget)
        self.v_username.setGeometry(QtCore.QRect(190, 60, 111, 17))
        self.v_username.setObjectName("v_username")
        self.usernameInput = QtWidgets.QLineEdit(self.centralwidget)
        self.usernameInput.setGeometry(QtCore.QRect(422, 60, 141, 25))
        self.usernameInput.setObjectName("usernameInput")
        self.editnameButton = QtWidgets.QPushButton(self.centralwidget)
        self.editnameButton.setGeometry(QtCore.QRect(590, 60, 89, 25))
        self.editnameButton.setObjectName("editnameButton")
        self.ssnLabel = QtWidgets.QLabel(self.centralwidget)
        self.ssnLabel.setGeometry(QtCore.QRect(70, 120, 71, 20))
        self.ssnLabel.setObjectName("ssnLabel")
        self.v_ssn = QtWidgets.QLabel(self.centralwidget)
        self.v_ssn.setGeometry(QtCore.QRect(190, 120, 111, 17))
        self.v_ssn.setObjectName("v_ssn")
        self.editssnButton = QtWidgets.QPushButton(self.centralwidget)
        self.editssnButton.setGeometry(QtCore.QRect(590, 120, 89, 25))
        self.editssnButton.setObjectName("editssnButton")
        self.phoneLabel = QtWidgets.QLabel(self.centralwidget)
        self.phoneLabel.setGeometry(QtCore.QRect(70, 170, 111, 20))
        self.phoneLabel.setObjectName("phoneLabel")
        self.phoneList = QtWidgets.QListWidget(self.centralwidget)
        self.phoneList.setGeometry(QtCore.QRect(70, 191, 291, 61))
        self.phoneList.setObjectName("phoneList")
        self.ssn_input = QtWidgets.QLineEdit(self.centralwidget)
        self.ssn_input.setGeometry(QtCore.QRect(420, 120, 141, 25))
        self.ssn_input.setObjectName("ssn_input")
        self.phone_input = QtWidgets.QLineEdit(self.centralwidget)
        self.phone_input.setGeometry(QtCore.QRect(420, 190, 141, 25))
        self.phone_input.setObjectName("phone_input")
        self.addphoneButton = QtWidgets.QPushButton(self.centralwidget)
        self.addphoneButton.setGeometry(QtCore.QRect(590, 190, 89, 25))
        self.addphoneButton.setObjectName("addphoneButton")
        self.removephoneButton = QtWidgets.QPushButton(self.centralwidget)
        self.removephoneButton.setGeometry(QtCore.QRect(590, 230, 89, 25))
        self.removephoneButton.setObjectName("removephoneButton")
        self.emailLabel = QtWidgets.QLabel(self.centralwidget)
        self.emailLabel.setGeometry(QtCore.QRect(70, 290, 111, 20))
        self.emailLabel.setObjectName("emailLabel")
        self.emailList = QtWidgets.QListWidget(self.centralwidget)
        self.emailList.setGeometry(QtCore.QRect(70, 311, 291, 61))
        self.emailList.setObjectName("emailList")
        self.removeemailButton = QtWidgets.QPushButton(self.centralwidget)
        self.removeemailButton.setGeometry(QtCore.QRect(590, 350, 89, 25))
        self.removeemailButton.setObjectName("removeemailButton")
        self.email_input = QtWidgets.QLineEdit(self.centralwidget)
        self.email_input.setGeometry(QtCore.QRect(420, 310, 141, 25))
        self.email_input.setText("")
        self.email_input.setObjectName("email_input")
        self.addemailButton = QtWidgets.QPushButton(self.centralwidget)
        self.addemailButton.setGeometry(QtCore.QRect(590, 310, 89, 25))
        self.addemailButton.setObjectName("addemailButton")
        self.bankLabel = QtWidgets.QLabel(self.centralwidget)
        self.bankLabel.setGeometry(QtCore.QRect(70, 420, 111, 20))
        self.bankLabel.setObjectName("bankLabel")
        self.bankList = QtWidgets.QListWidget(self.centralwidget)
        self.bankList.setGeometry(QtCore.QRect(70, 441, 291, 61))
        self.bankList.setObjectName("bankList")
        self.removebankButton = QtWidgets.QPushButton(self.centralwidget)
        self.removebankButton.setGeometry(QtCore.QRect(590, 480, 89, 25))
        self.removebankButton.setObjectName("removebankButton")
        self.bank_input = QtWidgets.QLineEdit(self.centralwidget)
        self.bank_input.setGeometry(QtCore.QRect(420, 440, 141, 25))
        self.bank_input.setObjectName("bank_input")
        self.addbankButton = QtWidgets.QPushButton(self.centralwidget)
        self.addbankButton.setGeometry(QtCore.QRect(590, 440, 89, 25))
        self.addbankButton.setObjectName("addbankButton")
        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setGeometry(QtCore.QRect(710, 520, 71, 25))
        self.backButton.setObjectName("backButton")
        AccountWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AccountWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 28))
        self.menubar.setObjectName("menubar")
        AccountWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AccountWindow)
        self.statusbar.setObjectName("statusbar")
        AccountWindow.setStatusBar(self.statusbar)

        self.retranslateUi(AccountWindow)
        QtCore.QMetaObject.connectSlotsByName(AccountWindow)

    def retranslateUi(self, AccountWindow):
        _translate = QtCore.QCoreApplication.translate
        AccountWindow.setWindowTitle(_translate("AccountWindow", "MainWindow"))
        self.usernameLabel.setText(_translate("AccountWindow", "Username:"))
        self.v_username.setText(_translate("AccountWindow", "v_username"))
        self.editnameButton.setText(_translate("AccountWindow", "Edit Name"))
        self.ssnLabel.setText(_translate("AccountWindow", "SSN:"))
        self.v_ssn.setText(_translate("AccountWindow", "v_ssn"))
        self.editssnButton.setText(_translate("AccountWindow", "Edit SSN"))
        self.phoneLabel.setText(_translate("AccountWindow", "Phone Number:"))
        self.addphoneButton.setText(_translate("AccountWindow", "Add"))
        self.removephoneButton.setText(_translate("AccountWindow", "Remove"))
        self.emailLabel.setText(_translate("AccountWindow", "Email Address:"))
        self.removeemailButton.setText(_translate("AccountWindow", "Remove"))
        self.addemailButton.setText(_translate("AccountWindow", "Add"))
        self.bankLabel.setText(_translate("AccountWindow", "Bank Account:"))
        self.removebankButton.setText(_translate("AccountWindow", "Remove"))
        self.addbankButton.setText(_translate("AccountWindow", "Add"))
        self.backButton.setText(_translate("AccountWindow", "Back"))


class AccountMenu(Ui_AccountWindow):
    def __init__(self, userId, db_conn):
        super(AccountMenu, self).__init__()
        self.userId = userId
        self.accountwindow=QMainWindow()
        self.setupUi(self.accountwindow)
        self.conn = db_conn
        cursor = self.conn.cursor()
        login = '''
            SELECT UserName from User 
            WHERE UserID = ?
        '''
        cursor.execute(login, [self.userId])
        uname = cursor.fetchall()
        self.v_username.setText(uname[0][0])
        # 绑定按钮点击后调用的函数
        self.editnameButton.clicked.connect(self.editNameFun)
        self.editssnButton.clicked.connect(self.editSSNFun)
        self.addphoneButton.clicked.connect(self.addPhoneFun)
        self.removephoneButton.clicked.connect(self.removePhoneFun)
        self.addemailButton.clicked.connect(self.addEmailFun)
        self.removeemailButton.clicked.connect(self.removeEmailFun)
        self.addbankButton.clicked.connect(self.addBankFuc)
        self.removebankButton.clicked.connect(self.removeBankFun)

        # 在这里查到电话、邮件、账号信息
        cursor.execute('''
                        SELECT Number FROM Phone
                        WHERE UserID = ?
                    ''', [self.userId])
        uphone = cursor.fetchall()
        print(uphone)
        cursor.execute('''
                                SELECT Address FROM Email
                                WHERE UserID = ?
                            ''', [self.userId])
        uemail = cursor.fetchall()
        print(uemail)
        cursor.execute('''
                                SELECT AccountNumber FROM UBRelation
                                WHERE UserID = ?
                            ''', [self.userId])
        ubank = cursor.fetchall()
        print(ubank)


    # 在下面编写按钮点击处理逻辑
    def editNameFun(self):
        value = self.usernameInput.text()
        if(len(value) > 0):
            cursor = self.conn.cursor()
            cursor.execute('''
                UPDATE USER
                SET UserName = ?
                WHERE UserID = ?
            ''', [value, self.userId])
            self.conn.commit()
        print("editNameFun")


    def editSSNFun(self):
        value = self.ssn_input.text()
        if (len(value) > 0):
            cursor = self.conn.cursor()
            cursor.execute('''
                        UPDATE USER
                        SET SSN = ?
                        WHERE UserID = ?
                    ''', [value, self.userId])
            self.conn.commit()
        print("editSSNFun")


    def addPhoneFun(self):
        # 这里可能还需要学习一下怎么读写pyqt5里面的QListWidget对象，邮件电话银行账户存在列表形式里
        value = self.phone_input.text()
        if (len(value) > 0):
            cursor = self.conn.cursor()
            cursor.execute('''
                        INSERT INTO Phone(UserID, Number, IsVerified)
                        VALUES (?, ?, 0)
                    ''', [self.userId, value])
            self.conn.commit()
        print("addPhoneFun")


    def removePhoneFun(self):
        value = self.phone_input.text()
        if (len(value) > 0):
            cursor = self.conn.cursor()
            cursor.execute('''
                               DELETE FROM Phone
                               WHERE UserID = ? and Number = ?
                           ''', [self.userId, value])
            self.conn.commit()
        print("removePhoneFun")


    def addEmailFun(self):
        value = self.email_input.text()
        if (len(value) > 0):
            cursor = self.conn.cursor()
            cursor.execute('''
                                INSERT INTO Email(UserID, Address, IsVerified)
                                VALUES (?, ?, 0)
                            ''', [self.userId, value])
            self.conn.commit()
        print("addEmailFun")


    def removeEmailFun(self):
        value = self.email_input.text()
        if (len(value) > 0):
            cursor = self.conn.cursor()
            cursor.execute('''
                                       DELETE FROM Email
                                       WHERE UserID = ? and Address = ?
                                   ''', [self.userId, value])
            self.conn.commit()
        print("removeEmailFun")


    def addBankFuc(self):
        value = self.bank_input.text()
        if (len(value) > 0):
            cursor = self.conn.cursor()
            cursor.execute('''
                            INSERT OR IGNORE INTO BankAccount(AccountNumber, IsVerified)
                            VALUES (?, 0)
                            ''', [value])
            self.conn.commit()
            cursor.execute('''
                            INSERT INTO UBRelation(UserID, AccountNumber)
                            VALUES (?, ?)
                            ''', [self.userId, value])
            self.conn.commit()
        print("addBankFuc")


    def removeBankFun(self):
        value = self.bank_input.text()
        if (len(value) > 0):
            cursor = self.conn.cursor()
            cursor.execute('''
                                               DELETE FROM UBRelation
                                               WHERE UserID = ? and AccountNumber = ?
                                           ''', [self.userId, value])
            self.conn.commit()
        print("removeBankFun")