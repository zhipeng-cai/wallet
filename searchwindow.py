# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'searchwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QDialog, QVBoxLayout, QListWidget, QListWidgetItem


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
        self.transactio_input.addItem("All")
        self.transactio_input.addItem("Send")
        self.transactio_input.addItem("Request")
        # Set the start date
        self.startDate.setDate(QDate(2023, 1, 1))
        # Set the end date
        self.endDate.setDate(QDate(2024, 1, 1))


class SearchMenu(Ui_SearchWindow):
    def __init__(self, userId, db_conn):
        super(SearchMenu, self).__init__()
        self.userId = userId
        self.searchwindow=QMainWindow()
        self.setupUi(self.searchwindow)
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


    def center_window(self):
        desktop = QDesktopWidget()

        screen_rect = desktop.screenGeometry()
        x = (screen_rect.width() - self.searchwindow.width()) // 2
        y = (screen_rect.height() - self.searchwindow.height()) // 2

        self.searchwindow.move(x, y)


    # 根据各个文本框的数据作为限制条件来查询
    # 可能要学习一下怎么读取QDateEdit对象的日期数据
    def searchFun(self):
        # Get the values from the input fields
        ssn = self.ssn_input.text().strip()
        email = self.email_input.text().strip()
        phone = self.phone_input.text().strip()
        transaction_type = self.transactio_input.currentText()
        transaction_type = None if transaction_type == "All" else transaction_type
        start_date = self.startDate.date().toString("yyyy-MM-dd") + " 00:00:00"
        end_date = self.endDate.date().toString("yyyy-MM-dd") + " 23:59:59"

        # Check if at least one of the five inputs is not empty
        if not any([ssn, email, phone, transaction_type, start_date, end_date]):
            print("Please provide at least one search criterion.")
            return

        # Construct the SQL query based on the provided constraints
        query = """
            SELECT Transactions.*,  strftime('%Y-%m-%d %H:%M:%S', Payment.PayTime) AS FormattedPayTime
            FROM Transactions
            LEFT JOIN Payment ON Transactions.TransactionID = Payment.TransactionID
            WHERE 1=1
        """

        # Prepare a list to store the parameters for the query
        params = []

        # Add constraints based on the provided input
        if ssn:
            query += " AND Transactions.InitiatorUserID IN (SELECT UserID FROM User WHERE SSN = ?)"
            params.append(ssn)

        if email:
            query += " AND Transactions.InitiatorUserID IN (SELECT UserID FROM Email WHERE Address = ?)"
            params.append(email)

        if phone:
            query += " AND Transactions.InitiatorUserID IN (SELECT UserID FROM Phone WHERE Number = ?)"
            params.append(phone)

        if transaction_type:
            query += " AND Transactions.Type = ?"
            params.append(transaction_type)

        # Adjust the query for the "PayTime" column in the "Payment" table
        query += " AND Payment.PayTime BETWEEN ? AND ?"
        params.extend([start_date, end_date])

        # Execute the query
        cursor = self.conn.cursor()
        cursor.execute(query, params)
        transactions = cursor.fetchall()

        # Process the search results (you can modify this based on your needs)
        # for transaction in transactions:
        #     print(transaction)  # You can replace this with the logic to display or process the search results

        # Display the search results in a new dialog
        results_dialog = QDialog()
        results_dialog.setWindowTitle("Search Results")
        results_dialog.setGeometry(100, 100, 500, 300)

        # Create a QVBoxLayout for the dialog
        layout = QVBoxLayout(results_dialog)

        # Create a QListWidget to display the search results
        list_widget = QListWidget(results_dialog)

        # Add each transaction as an item in the QListWidget
        for transaction in transactions:
            item_text = f"Transaction {transaction[0]}: {transaction[1]} - {transaction[2]} - {transaction[3]} - {transaction[4]}"
            list_item = QListWidgetItem(item_text)
            list_widget.addItem(list_item)

        # Add the QListWidget to the layout
        layout.addWidget(list_widget)

        # Center the dialo
        desktop = QDesktopWidget()
        screen_rect = desktop.screenGeometry()
        x = screen_rect.x() + (screen_rect.width() - results_dialog.width()) / 2
        y = screen_rect.y() + (screen_rect.height() - results_dialog.height()) / 2
        results_dialog.move(x, y)

        # Show the dialog
        results_dialog.exec_()
