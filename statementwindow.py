# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'statementwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget


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
        self.answer1.setGeometry(QtCore.QRect(380, 133, 331, 17))
        self.answer1.setObjectName("answer1")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(80, 190, 521, 17))
        self.label_6.setObjectName("label_6")
        self.answer2List = QtWidgets.QListWidget(self.centralwidget)
        self.answer2List.setGeometry(QtCore.QRect(80, 220, 461, 81))
        self.answer2List.setObjectName("answer2List")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(80, 330, 521, 17))
        self.label_7.setObjectName("label_7")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(80, 450, 601, 17))
        self.label_9.setObjectName("label_9")
        self.answer4 = QtWidgets.QLabel(self.centralwidget)
        self.answer4.setGeometry(QtCore.QRect(80, 470, 521, 35))
        self.answer4.setObjectName("answer4")
        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setGeometry(QtCore.QRect(730, 520, 61, 25))
        self.backButton.setObjectName("backButton")
        self.searchButton = QtWidgets.QPushButton(self.centralwidget)
        self.searchButton.setGeometry(QtCore.QRect(300, 131, 61, 25))
        self.searchButton.setObjectName("searchButton")
        self.answer3List = QtWidgets.QListWidget(self.centralwidget)
        self.answer3List.setGeometry(QtCore.QRect(80, 350, 461, 81))
        self.answer3List.setObjectName("answer3List")
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
        self.label_9.setText(_translate("StatementWindow", "4. The best users (users who have sent/received the maximum total amount of money):"))
        self.answer4.setText(_translate("StatementWindow", "no result"))
        self.backButton.setText(_translate("StatementWindow", "Back"))
        self.searchButton.setText(_translate("StatementWindow", "Search"))
        # Set the start date
        self.startDate.setDate(QDate(2023, 1, 1))
        # Set the end date
        self.endDate.setDate(QDate(2024, 1, 1))


class StatementMenu(Ui_StatementWindow):
    def __init__(self, userId, db_conn):
        super(StatementMenu, self).__init__()
        self.userId = userId
        self.statementwindow=QMainWindow()
        self.setupUi(self.statementwindow)
        self.center_window()
        self.conn = db_conn
        cursor = self.conn.cursor()
        login = '''
                    SELECT UserName from User 
                    WHERE UserID = ?
                '''
        cursor.execute(login, [self.userId])
        uname = cursor.fetchall()
        self.usernameLabel.setText(uname[0][0])
        # 绑定按钮点击后调用的函数
        self.searchButton.clicked.connect(self.searchFun)
        # 这个页面还有很多不用点击按钮触发的数据库读写逻辑，需要页面一加载出来就把读取到的指标显示在对应的Label组件上，分别是answe1, answer2, answer3, answer4
        # implement code here to read the database to get the answer and set the label text to the answer
        # Load and display the answers
        self.load_and_display_answers()

    def load_and_display_answers(self):
        # Call the methods to load and display answers for each query
        self.load_and_display_answer1()
        self.load_and_display_answer2()
        self.load_and_display_answer3()
        self.load_and_display_answer4()

    def load_and_display_answer1(self):
        cursor = self.conn.cursor()

        # Query the total amount of money sent by the user in the specified date range
        send_query = """
                    SELECT SUM(Amount) AS TotalAmount
                    FROM Payment
                    WHERE SenderUserID = ?
                        AND PayTime BETWEEN ? AND ?
                """

        # Query the total amount of money received by the user in the specified date range
        receive_query = """
                    SELECT SUM(Amount) AS TotalAmount
                    FROM Payment
                    WHERE ReceiverUserID = ?
                        AND PayTime BETWEEN ? AND ?
                """

        start_date = self.startDate.date().toString("yyyy-MM-dd") + " 00:00:00"
        end_date = self.endDate.date().toString("yyyy-MM-dd") + " 23:59:59"

        params = [self.userId, start_date, end_date]

        # Fetch and display the total amount sent
        cursor.execute(send_query, params)
        send_result = cursor.fetchone()
        send_amount = send_result[0] if send_result and send_result[0] is not None else 0

        # Fetch and display the total amount received
        cursor.execute(receive_query, params)
        receive_result = cursor.fetchone()
        receive_amount = receive_result[0] if receive_result and receive_result[0] is not None else 0

        # Display the results in the labels
        answer_text = f"Sent: {send_amount}\tReceived: {receive_amount}"
        self.answer1.setText(answer_text)


    def load_and_display_answer2(self):
        cursor = self.conn.cursor()

        # Query the total amount of money sent and received by the user per month
        query = """
                    SELECT strftime('%Y-%m', PayTime) AS Month,
                           SUM(CASE WHEN SenderUserID = ? THEN Amount ELSE 0 END) AS SentAmount,
                           SUM(CASE WHEN ReceiverUserID = ? THEN Amount ELSE 0 END) AS ReceivedAmount
                    FROM Payment
                    WHERE SenderUserID = ? OR ReceiverUserID = ?
                    GROUP BY Month
                    ORDER BY Month
                """

        params = [self.userId, self.userId, self.userId, self.userId]

        # Fetch the results
        cursor.execute(query, params)
        results = cursor.fetchall()

        # Display the results in the list widget
        self.answer2List.clear()
        for result in results:
            month, sent_amount, received_amount = result
            answer_text = f"Month: {month}, Sent: {sent_amount}, Received: {received_amount}"
            self.answer2List.addItem(answer_text)


    def load_and_display_answer3(self):
        cursor = self.conn.cursor()

        # Query transactions with the maximum amount of money per month for the user
        query = """
                    SELECT strftime('%Y-%m', PayTime) AS Month,
                           MAX(Amount) AS MaxAmount
                    FROM Payment
                    WHERE SenderUserID = ? OR ReceiverUserID = ?
                    GROUP BY Month
                    ORDER BY Month
                """

        params = [self.userId, self.userId]

        # Fetch the results
        cursor.execute(query, params)
        results = cursor.fetchall()

        # Display the results in the list widget
        self.answer3List.clear()
        for result in results:
            month, max_amount = result
            answer_text = f"Month: {month}, Max Amount: {max_amount}"
        self.answer3List.addItem(answer_text)

    def load_and_display_answer4(self):
        # Implement the logic to fetch answer for query 4 and set the label text
        answer = "no result"  # Replace this with the actual answer

        # Query to find the user who has sent the maximum total amount of money
        query_sent = """
            SELECT UserID, UserName, COALESCE(SUM(TotalAmount), 0) AS SentAmount
            FROM User
            LEFT JOIN Transactions ON User.UserID = Transactions.InitiatorUserID
            WHERE Transactions.TotalAmount > 0 AND Transactions.Type = 'Send'
            GROUP BY User.UserID, User.UserName
            ORDER BY SentAmount DESC
            LIMIT 1;
        """

        # Query to find the user who has received the maximum total amount of money (Request type)
        query_received = """
            SELECT UserID, UserName, COALESCE(SUM(TotalAmount), 0) AS ReceivedAmount
            FROM User
            LEFT JOIN Transactions ON User.UserID = Transactions.InitiatorUserID
            WHERE Transactions.TotalAmount > 0 AND Transactions.Type = 'Request'
            GROUP BY User.UserID, User.UserName
            ORDER BY ReceivedAmount DESC
            LIMIT 1;
        """

        cursor = self.conn.cursor()

        # Execute the query for the user who has sent the most money
        cursor.execute(query_sent)
        result_sent = cursor.fetchone()

        # Execute the query for the user who has received the most money (Request type)
        cursor.execute(query_received)
        result_received = cursor.fetchone()

        # print(result_sent)
        # print(result_received)
        if result_sent and result_received:
            answer = f" User who sent the most: {result_sent[0]} ({result_sent[1]}) - {result_sent[2]} \n " \
                     f"User who received the most: {result_received[0]} ({result_received[1]}) - {result_received[2]}"
        elif result_sent:
            answer = f"User who sent the most: {result_sent[0]} ({result_sent[1]}) - {result_sent[2]}"
        elif result_received:
            answer = f"User who received the most (Request type): {result_received[0]} ({result_received[1]}) - {result_received[2]}"
        else:
            answer = "No result"

        # Set the label text with the answer
        self.answer4.setText(answer)


    def center_window(self):
        desktop = QDesktopWidget()

        screen_rect = desktop.screenGeometry()
        x = (screen_rect.width() - self.statementwindow.width()) // 2
        y = (screen_rect.height() - self.statementwindow.height()) // 2

        self.statementwindow.move(x, y)


    def searchFun(self):
        self.load_and_display_answer1()
        print("searchFun")