# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!
from datetime import datetime

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget

from dialogutil import open_dialog


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
    def __init__(self, userId, db_conn):
        super(MainMenu, self).__init__()
        self.userId = userId
        self.mainwindow=QMainWindow()
        self.setupUi(self.mainwindow)
        self.center_window()
        self.conn = db_conn
        cursor = self.conn.cursor()
        login = '''
                    SELECT UserName from User 
                    WHERE UserID = ?
                '''
        cursor.execute(login, [self.userId])
        uname = cursor.fetchall()
        self.label_2.setText(uname[0][0])
        # 绑定按钮点击后调用的函数
        self.sendButton.clicked.connect(self.sendMoneyFun)
        self.requestButton.clicked.connect(self.requestMoneyFun)


    def center_window(self):
        desktop = QDesktopWidget()

        screen_rect = desktop.screenGeometry()
        x = (screen_rect.width() - self.mainwindow.width()) // 2
        y = (screen_rect.height() - self.mainwindow.height()) // 2

        self.mainwindow.move(x, y)


    # 在下面编写按钮点击处理逻辑
    def sendMoneyFun(self):
        # 获取文本输入框的值 输入文本框是QLineEdit对象
        phoneOrEmail = self.sendPhone.text()
        money_input = self.sendMoney.text()

        if not phoneOrEmail:
            open_dialog("用户不能为空", 100, 50, 300, 200)
            print("Phone or email cannot be empty.")
            return

        try:
            money = int(money_input) if money_input else 0
        except ValueError:
            open_dialog("请输入有效金额", 100, 50, 300, 200)
            print("Invalid money input. Please enter a valid number.")
            return
        # 读取数据, call conn.commit() if make any changes to the database
        cursor = self.conn.cursor()
        # Step 1: Get the sender's information. i.e., self.userId
        sender_id = self.userId

        # Step 2: Determine the receiver's information based on phoneOrEmail
        cursor.execute(
            "SELECT UserID FROM User WHERE UserID IN (SELECT UserID FROM Email WHERE Address = ? OR UserID IN (SELECT UserID FROM Phone WHERE Number = ?))",
            (phoneOrEmail, phoneOrEmail))
        receiver_info = cursor.fetchone()

        if receiver_info is None:
            open_dialog("用户不存在", 125, 50, 300, 200)
            print("Receiver not found.")
            return

        receiver_id = receiver_info[0]

        # Step 3: Check the sender's bank accounts in priority order
        cursor.execute("""
            SELECT UBRelation.UserID, UBRelation.AccountNumber, BankAccount.Balance
            FROM UBRelation
            JOIN BankAccount ON UBRelation.AccountNumber = BankAccount.AccountNumber
            WHERE UBRelation.UserID = ?
            ORDER BY BankAccount.Priority
        """, (sender_id,))

        user_banks = cursor.fetchall()

        for user_bank in user_banks:
            _, account_number, balance = user_bank

            if balance >= money:  # Check if the account balance is enough
                # Step 4: Create a new transaction record
                cursor.execute("""
                    INSERT INTO Transactions (InitiatorUserID, Type, TotalAmount)
                    VALUES (?, ?, ?)
                """, (sender_id, 'Send', money))

                transaction_id = cursor.lastrowid

                # Step 5: Create a new payment record
                cursor.execute("""
                    INSERT INTO Payment (SenderUserID, ReceiverUserID, TransactionID, Amount, Memo, PayTime, IsSuccessful)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                """, (sender_id, receiver_id, transaction_id, money,
                      f"Payment from {sender_id} to {receiver_id}", datetime.now(), 1))

                # Step 6: Update sender's bank account balance
                cursor.execute("""
                                UPDATE BankAccount
                                SET Balance = Balance - ?
                                WHERE AccountNumber = ?
                            """, (money, account_number))

                # Step 7: Update receiver's bank account balance (using the bank account with the highest priority)
                cursor.execute("""
                    UPDATE BankAccount
                    SET Balance = Balance + ?
                    WHERE AccountNumber = (
                        SELECT BankAccount.AccountNumber
                        FROM UBRelation
                        JOIN BankAccount ON UBRelation.AccountNumber = BankAccount.AccountNumber
                        WHERE UBRelation.UserID = ?
                        ORDER BY BankAccount.Priority DESC
                        LIMIT 1
                    )
                """, (money, receiver_id))
                # Commit the changes
                self.conn.commit()
                open_dialog("转账成功", 125, 50, 300, 200)
                print(f"Transaction successful! {money} sent from {sender_id} to {receiver_id} using account {account_number}")
                return

        open_dialog("余额不足", 125, 50, 300, 200)
        print("No suitable bank account found with enough balance.")
        print("sendMoney")

    def requestMoneyFun(self):
        # Get values from text input boxes (QLineEdit objects)
        phoneOrEmail = self.requestPhone.text()
        money_input = self.requestMoney.text()

        if not phoneOrEmail:
            open_dialog("用户不能为空", 100, 50, 300, 200)
            print("Phone or email cannot be empty.")
            return

        try:
            money = int(money_input) if money_input else 0
        except ValueError:
            open_dialog("请输入有效金额", 100, 50, 300, 200)
            print("Invalid money input. Please enter a valid number.")
            return

        # Read data, call conn.commit() if there are any changes to the database
        cursor = self.conn.cursor()

        # Step 1: Get the receiver's information, i.e., self.userId
        receiver_id = self.userId

        # Step 2: Determine the sender's information based on phoneOrEmail
        cursor.execute("""
            SELECT UserID
            FROM User
            WHERE UserID IN (SELECT UserID FROM Email WHERE Address = ? OR UserID IN (SELECT UserID FROM Phone WHERE Number = ?))
        """, (phoneOrEmail, phoneOrEmail))
        sender_info = cursor.fetchone()

        if sender_info is None:
            open_dialog("用户不存在", 125, 50, 300, 200)
            print("Sender not found.")
            return

        sender_id = sender_info[0]

        # Step 3: Check the sender's bank accounts in priority order
        cursor.execute("""
            SELECT UBRelation.UserID, UBRelation.AccountNumber, BankAccount.Balance, BankAccount.Priority
            FROM UBRelation
            JOIN BankAccount ON UBRelation.AccountNumber = BankAccount.AccountNumber
            WHERE UBRelation.UserID = ?
            ORDER BY BankAccount.Priority
        """, (sender_id,))

        user_banks = cursor.fetchall()

        for user_bank in user_banks:
            _, account_number, balance, priority = user_bank

            if balance >= money:  # Check if the account balance is enough
                # Step 4: Update sender's bank account balance
                cursor.execute("""
                    UPDATE BankAccount
                    SET Balance = Balance - ?
                    WHERE AccountNumber = ?
                """, (money, account_number))

                # Step 5: Update receiver's bank account balance (using the bank account with the highest priority)
                cursor.execute("""
                    UPDATE BankAccount
                    SET Balance = Balance + ?
                    WHERE AccountNumber = (
                        SELECT BankAccount.AccountNumber
                        FROM UBRelation
                        JOIN BankAccount ON UBRelation.AccountNumber = BankAccount.AccountNumber
                        WHERE UBRelation.UserID = ?
                        ORDER BY BankAccount.Priority DESC
                        LIMIT 1
                    )
                """, (money, receiver_id))

                # Step 6: Create a new transaction record
                cursor.execute("""
                    INSERT INTO Transactions (InitiatorUserID, Type, TotalAmount)
                    VALUES (?, ?, ?)
                """, (receiver_id, 'Request', money))

                transaction_id = cursor.lastrowid

                # Step 7: Create a new payment record
                cursor.execute("""
                    INSERT INTO Payment (SenderUserID, ReceiverUserID, TransactionID, Amount, Memo, PayTime, IsSuccessful)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                """, (sender_id, receiver_id, transaction_id, money,
                      f"Payment from {sender_id} to {receiver_id}", datetime.now(), 1))

                # Commit the changes
                self.conn.commit()
                open_dialog("请求成功", 125, 50, 300, 200)
                print(
                    f"Request successful! {money} requested by {receiver_id} from {sender_id} using account {account_number}")
                return

        open_dialog("对方余额不足", 100, 50, 300, 200)
        print("No suitable bank account found with enough balance.")
        print("requestMoney")


    def clear(self):
        self.sendPhone.clear()
        self.sendMoney.clear()
        self.requestPhone.clear()
        self.requestMoney.clear()
