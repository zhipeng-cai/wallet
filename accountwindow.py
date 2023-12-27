# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'accountwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QListWidgetItem
from dialogutil import open_dialog


class Ui_AccountWindow(object):
    def setupUi(self, AccountWindow):
        AccountWindow.setObjectName("AccountWindow")
        AccountWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(AccountWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.passwordLabel = QtWidgets.QLabel(self.centralwidget)
        self.passwordLabel.setGeometry(QtCore.QRect(70, 70, 71, 17))
        self.passwordLabel.setObjectName("passwordLabel")
        self.v_password = QtWidgets.QLabel(self.centralwidget)
        self.v_password.setGeometry(QtCore.QRect(190, 70, 111, 17))
        self.v_password.setObjectName("v_password")
        self.passwordInput = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordInput.setGeometry(QtCore.QRect(420, 70, 141, 25))
        self.passwordInput.setObjectName("passwordInput")
        self.editpasswordButton = QtWidgets.QPushButton(self.centralwidget)
        self.editpasswordButton.setGeometry(QtCore.QRect(590, 70, 111, 25))
        self.editpasswordButton.setObjectName("editpasswordButton")
        self.ssnLabel = QtWidgets.QLabel(self.centralwidget)
        self.ssnLabel.setGeometry(QtCore.QRect(70, 120, 71, 20))
        self.ssnLabel.setObjectName("ssnLabel")
        self.v_ssn = QtWidgets.QLabel(self.centralwidget)
        self.v_ssn.setGeometry(QtCore.QRect(190, 120, 111, 17))
        self.v_ssn.setObjectName("v_ssn")
        self.editssnButton = QtWidgets.QPushButton(self.centralwidget)
        self.editssnButton.setGeometry(QtCore.QRect(590, 120, 111, 25))
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
        self.bankLabel.setGeometry(QtCore.QRect(70, 420, 300, 20))
        self.bankLabel.setObjectName("bankLabel")
        self.bankList = QtWidgets.QListWidget(self.centralwidget)
        self.bankList.setGeometry(QtCore.QRect(70, 441, 291, 61))
        self.bankList.setObjectName("bankList")
        self.removebankButton = QtWidgets.QPushButton(self.centralwidget)
        self.removebankButton.setGeometry(QtCore.QRect(590, 480, 89, 25))
        self.removebankButton.setObjectName("removebankButton")
        self.banknumber_input = QtWidgets.QLineEdit(self.centralwidget)
        self.banknumber_input.setGeometry(QtCore.QRect(420, 440, 141, 25))
        self.banknumber_input.setObjectName("banknumber_input")
        self.addbankButton = QtWidgets.QPushButton(self.centralwidget)
        self.addbankButton.setGeometry(QtCore.QRect(590, 440, 89, 25))
        self.addbankButton.setObjectName("addbankButton")
        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setGeometry(QtCore.QRect(710, 520, 71, 25))
        self.backButton.setObjectName("backButton")
        self.usernameLabel = QtWidgets.QLabel(self.centralwidget)
        self.usernameLabel.setGeometry(QtCore.QRect(70, 20, 71, 17))
        self.usernameLabel.setObjectName("usernameLabel")
        self.usernameInput = QtWidgets.QLineEdit(self.centralwidget)
        self.usernameInput.setGeometry(QtCore.QRect(420, 20, 141, 25))
        self.usernameInput.setObjectName("usernameInput")
        self.editnameButton = QtWidgets.QPushButton(self.centralwidget)
        self.editnameButton.setGeometry(QtCore.QRect(590, 20, 111, 25))
        self.editnameButton.setObjectName("editnameButton")
        self.v_username = QtWidgets.QLabel(self.centralwidget)
        self.v_username.setGeometry(QtCore.QRect(190, 20, 111, 17))
        self.v_username.setObjectName("v_username")
        self.bankbalance_input = QtWidgets.QLineEdit(self.centralwidget)
        self.bankbalance_input.setGeometry(QtCore.QRect(420, 470, 141, 25))
        self.bankbalance_input.setObjectName("bankbalance_input")
        self.bankpriority_input = QtWidgets.QLineEdit(self.centralwidget)
        self.bankpriority_input.setGeometry(QtCore.QRect(420, 500, 141, 25))
        self.bankpriority_input.setObjectName("bankpriority_input")
        self.banknumberLabel = QtWidgets.QLabel(self.centralwidget)
        self.banknumberLabel.setGeometry(QtCore.QRect(360, 440, 67, 17))
        self.banknumberLabel.setObjectName("banknumberLabel")
        self.bankbalanceLabel = QtWidgets.QLabel(self.centralwidget)
        self.bankbalanceLabel.setGeometry(QtCore.QRect(360, 470, 67, 17))
        self.bankbalanceLabel.setObjectName("bankbalanceLabel")
        self.bankpriorityLabel = QtWidgets.QLabel(self.centralwidget)
        self.bankpriorityLabel.setGeometry(QtCore.QRect(360, 500, 67, 17))
        self.bankpriorityLabel.setObjectName("bankpriorityLabel")
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
        self.passwordLabel.setText(_translate("AccountWindow", "Password:"))
        self.v_password.setText(_translate("AccountWindow", "********"))
        self.editpasswordButton.setText(_translate("AccountWindow", "Edit Password"))
        self.ssnLabel.setText(_translate("AccountWindow", "SSN:"))
        self.v_ssn.setText(_translate("AccountWindow", "v_ssn"))
        self.editssnButton.setText(_translate("AccountWindow", "Edit SSN"))
        self.phoneLabel.setText(_translate("AccountWindow", "Phone Number:"))
        self.addphoneButton.setText(_translate("AccountWindow", "Add"))
        self.removephoneButton.setText(_translate("AccountWindow", "Remove"))
        self.emailLabel.setText(_translate("AccountWindow", "Email Address:"))
        self.removeemailButton.setText(_translate("AccountWindow", "Remove"))
        self.addemailButton.setText(_translate("AccountWindow", "Add"))
        self.bankLabel.setText(_translate("AccountWindow", "Bank Account:[Number](Balance)(Priority)"))
        self.removebankButton.setText(_translate("AccountWindow", "Remove"))
        self.addbankButton.setText(_translate("AccountWindow", "Add"))
        self.backButton.setText(_translate("AccountWindow", "Back"))
        self.usernameLabel.setText(_translate("AccountWindow", "Username:"))
        self.editnameButton.setText(_translate("AccountWindow", "Edit Name"))
        self.v_username.setText(_translate("AccountWindow", "v_username"))
        self.banknumberLabel.setText(_translate("AccountWindow", "Number"))
        self.bankbalanceLabel.setText(_translate("AccountWindow", "Balance"))
        self.bankpriorityLabel.setText(_translate("AccountWindow", "Priority"))


class AccountMenu(Ui_AccountWindow):
    def __init__(self, userId, db_conn):
        super(AccountMenu, self).__init__()
        self.userId = userId
        self.accountwindow=QMainWindow()
        self.setupUi(self.accountwindow)
        self.center_window()
        self.conn = db_conn
        cursor = self.conn.cursor()
        login = '''
            SELECT UserName, SSN from User 
            WHERE UserID = ?
        '''
        cursor.execute(login, [self.userId])
        uname = cursor.fetchall()
        self.v_username.setText(uname[0][0])
        self.v_ssn.setText(uname[0][1])
        # 绑定按钮点击后调用的函数
        self.editnameButton.clicked.connect(self.editNameFun)
        self.editpasswordButton.clicked.connect(self.editPasswordFun)
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
        for phone_number in uphone:
            item = QListWidgetItem(str(phone_number[0]))
            self.phoneList.addItem(item)


        cursor.execute('''
                                SELECT Address FROM Email
                                WHERE UserID = ?
                            ''', [self.userId])
        uemail = cursor.fetchall()
        for email in uemail:
            item = QListWidgetItem(str(email[0]))
            self.emailList.addItem(item)

        cursor.execute('''
            SELECT BA.AccountNumber, BA.Balance, BA.Priority
            FROM BankAccount AS BA
            JOIN UBRelation AS UBR ON BA.AccountNumber = UBR.AccountNumber
            WHERE UBR.UserID = ?
        ''', [self.userId])
        ubank = cursor.fetchall()
        for bank in ubank:
            item = QListWidgetItem("{}    ({}) ({})".format(bank[0], bank[1], bank[2]))
            self.bankList.addItem(item)


    def center_window(self):
        desktop = QDesktopWidget()

        screen_rect = desktop.screenGeometry()
        x = (screen_rect.width() - self.accountwindow.width()) // 2
        y = (screen_rect.height() - self.accountwindow.height()) // 2

        self.accountwindow.move(x, y)


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
            self.v_username.setText(value)
            self.usernameInput.clear()
            open_dialog("修改成功", 125, 50, 300, 200)
        print("editNameFun")


    def editPasswordFun(self):
        value = self.passwordInput.text()
        if (len(value) > 0):
            cursor = self.conn.cursor()
            cursor.execute('''
                        UPDATE USER
                        SET PassWord = ?
                        WHERE UserID = ?
                    ''', [value, self.userId])
            self.conn.commit()
            self.passwordInput.clear()
            open_dialog("修改成功", 125, 50, 300, 200)
        print("editPasswordFun")


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
            self.v_ssn.setText(value)
            self.ssn_input.clear()
            open_dialog("修改成功", 125, 50, 300, 200)
        print("editSSNFun")


    def addPhoneFun(self):
        # 这里可能还需要学习一下怎么读写pyqt5里面的QListWidget对象，邮件电话银行账户存在列表形式里
        value = self.phone_input.text()
        if (len(value) > 0):
            cursor = self.conn.cursor()
            cursor.execute('''
                        SELECT SUM(Amount) FROM Payment
                        WHERE IsSuccessful = 2 AND Memo = ?
                    ''', [value])
            results = cursor.fetchall()
            if(len(results) > 0 and (not results[0][0] is None)):
                cursor.execute("""
                            SELECT BankAccount.AccountNumber
                            FROM UBRelation
                            JOIN BankAccount ON UBRelation.AccountNumber = BankAccount.AccountNumber
                            WHERE UBRelation.UserID = ?
                            ORDER BY BankAccount.Priority DESC
                            LIMIT 1
                        """, (self.userId,))
                user_banks = cursor.fetchall()
                if(len(user_banks) == 0):
                    open_dialog("无效账号", 125, 50, 300, 200)
                    return
                cursor.execute("""
                                    UPDATE BankAccount
                                    SET Balance = Balance + ?
                                    WHERE AccountNumber = ?
                                """, (results[0][0], user_banks[0][0]))
                cursor.execute('''
                                        UPDATE Payment
                                        SET IsSuccessful = 1 
                                        WHERE IsSuccessful = 2 AND Memo = ?
                                    ''', [value])

            cursor.execute('''
                        INSERT INTO Phone(UserID, Number, IsVerified)
                        VALUES (?, ?, 0)
                    ''', [self.userId, value])
            self.conn.commit()
            self.phoneList.addItem(QListWidgetItem(value))
            self.phone_input.clear()
            open_dialog("添加成功", 125, 50, 300, 200)
        print("addPhoneFun")


    def removePhoneFun(self):
        value = self.phone_input.text()
        if len(value) == 0:
            selected_item = self.phoneList.currentItem()
            if selected_item:
                value = selected_item.text()
        if (len(value) > 0):
            cursor = self.conn.cursor()
            cursor.execute('''
                               DELETE FROM Phone
                               WHERE UserID = ? and Number = ?
                           ''', [self.userId, value])
            self.conn.commit()
            item_to_remove = None
            for index in range(self.phoneList.count()):
                item = self.phoneList.item(index)
                if item.text() == value:
                    item_to_remove = item
                    break
            if item_to_remove:
                self.phoneList.takeItem(self.phoneList.row(item_to_remove))
                self.phone_input.clear()
                open_dialog("删除成功", 125, 50, 300, 200)
        print("removePhoneFun")


    def addEmailFun(self):
        value = self.email_input.text()
        if (len(value) > 0):
            cursor = self.conn.cursor()
            cursor.execute('''
                                    SELECT SUM(Amount) FROM Payment
                                    WHERE IsSuccessful = 2 AND Memo = ?
                                ''', [value])
            results = cursor.fetchall()
            if (len(results) > 0 and (not results[0][0] is None)):
                cursor.execute("""
                                        SELECT BankAccount.AccountNumber
                                        FROM UBRelation
                                        JOIN BankAccount ON UBRelation.AccountNumber = BankAccount.AccountNumber
                                        WHERE UBRelation.UserID = ?
                                        ORDER BY BankAccount.Priority DESC
                                        LIMIT 1
                                    """, (self.userId,))
                user_banks = cursor.fetchall()
                if (len(user_banks) == 0):
                    open_dialog("无效账号", 125, 50, 300, 200)
                    return
                cursor.execute("""
                                                UPDATE BankAccount
                                                SET Balance = Balance + ?
                                                WHERE AccountNumber = ?
                                            """, (results[0][0], user_banks[0][0]))
                cursor.execute('''
                                                    UPDATE Payment
                                                    SET IsSuccessful = 1 
                                                    WHERE IsSuccessful = 2 AND Memo = ?
                                                ''', [value])

            cursor.execute('''
                                INSERT INTO Email(UserID, Address, IsVerified)
                                VALUES (?, ?, 0)
                            ''', [self.userId, value])
            self.conn.commit()
            self.emailList.addItem(QListWidgetItem(value))
            self.email_input.clear()
            open_dialog("添加成功", 125, 50, 300, 200)
        print("addEmailFun")


    def removeEmailFun(self):
        value = self.email_input.text()
        if len(value) == 0:
            selected_item = self.emailList.currentItem()
            if selected_item:
                value = selected_item.text()
        if (len(value) > 0):
            cursor = self.conn.cursor()
            cursor.execute('''
                                       DELETE FROM Email
                                       WHERE UserID = ? and Address = ?
                                   ''', [self.userId, value])
            self.conn.commit()
            item_to_remove = None
            for index in range(self.emailList.count()):
                item = self.emailList.item(index)
                if item.text() == value:
                    item_to_remove = item
                    break
            if item_to_remove:
                self.emailList.takeItem(self.emailList.row(item_to_remove))
                self.email_input.clear()
                open_dialog("删除成功", 125, 50, 300, 200)
        print("removeEmailFun")


    def addBankFuc(self):
        banknumber = self.banknumber_input.text()
        bankbalance = self.bankbalance_input.text()
        bankpriority = self.bankpriority_input.text()
        if (len(banknumber) > 0 and len(bankbalance) > 0 and len(bankpriority) > 0):
            cursor = self.conn.cursor()
            cursor.execute('''
                            INSERT OR IGNORE INTO BankAccount(AccountNumber, Balance, Priority, IsVerified)
                            VALUES (?, ?, ?, 0)
                            ''', [banknumber, bankbalance, bankpriority])
            cursor.execute('''
                            INSERT INTO UBRelation(UserID, AccountNumber)
                            VALUES (?, ?)
                            ''', [self.userId, banknumber])
            self.conn.commit()
            self.bankList.addItem(QListWidgetItem("{}    ({}) ({})".format(banknumber, bankbalance, bankpriority)))
            self.banknumber_input.clear()
            self.bankbalance_input.clear()
            self.bankpriority_input.clear()
            open_dialog("添加成功", 125, 50, 300, 200)
        print("addBankFuc")


    def removeBankFun(self):
        value = self.banknumber_input.text()
        if len(value) == 0:
            selected_item = self.bankList.currentItem()
            if selected_item:
                value = selected_item.text().split(' ')[0]
        if (len(value) > 0):
            print(value)
            cursor = self.conn.cursor()
            cursor.execute('''
                                               DELETE FROM UBRelation
                                               WHERE UserID = ? and AccountNumber = ?
                                           ''', [self.userId, value])
            self.conn.commit()
            item_to_remove = None
            for index in range(self.bankList.count()):
                item = self.bankList.item(index)
                if item.text().split(' ')[0] == value:
                    item_to_remove = item
                    break
            if item_to_remove:
                self.bankList.takeItem(self.bankList.row(item_to_remove))
                self.banknumber_input.clear()
                self.bankbalance_input.clear()
                self.bankpriority_input.clear()
                open_dialog("删除成功", 125, 50, 300, 200)
        print("removeBankFun")