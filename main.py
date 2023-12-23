import os

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sqlite3
import dbInit
from loginwindow import LoginMenu
from mainwindow import MainMenu
from accountwindow import AccountMenu
from statementwindow import StatementMenu
from searchwindow import SearchMenu


class Main():
    def __init__(self):
        self.login_menu = LoginMenu(self)
        self.login_menu.loginButton.clicked.connect(self.logining)
        self.login_menu.loginwindow.show()

        # Connect to the SQLite database (this will create a new database file if it doesn't exist)
        db_file_path = './db/data.db'
        if os.path.exists(db_file_path):
            os.remove(db_file_path)
        self.conn = sqlite3.connect(db_file_path)  # 数据库连接，把这个变量传给其它需要使用数据库的函数
        dbInit.create_tables(self.conn)
        dbInit.insert_init_data(self.conn)

    # 页面跳转的按钮点击逻辑在main.py 读写数据库的在各自的窗口文件
    def logining(self):
        self.username = self.login_menu.usernameInput.text()
        self.password = self.login_menu.passwordInput.text()

        cursor = self.conn.cursor()
        login = '''
            SELECT UserID from User 
            WHERE UserName = ? and SSN = ?
        '''
        cursor.execute(login, [self.username, self.password])
        uid = cursor.fetchall()
        if(len(uid) == 0):
            print('login failed')
            #ZHANGXIHAO 改成在页面上显示登录失败
            return
        self.userId = uid[0][0]

        self.main_menu = MainMenu(self.userId, self.conn)
        self.main_menu.accountButton.clicked.connect(self.toAccountPage)
        self.main_menu.statementButton.clicked.connect(self.toStatementPage)
        self.main_menu.transactionButton.clicked.connect(self.toSearchPage)
        self.main_menu.signoutButton.clicked.connect(self.loginout)

        self.login_menu.loginwindow.close()
        self.main_menu.mainwindow.show()

    def loginout(self):
        self.username = ""
        self.password = ""
        self.login_menu.usernameInput.clear()
        self.login_menu.passwordInput.clear()
        self.main_menu.mainwindow.close()
        self.login_menu.loginwindow.show()

    def toAccountPage(self):
        self.account_menu = AccountMenu(self.userId, self.conn)
        self.account_menu.backButton.clicked.connect(self.backFromAccount)

        self.main_menu.mainwindow.close()
        self.account_menu.accountwindow.show()

    def backFromAccount(self):
        self.account_menu.accountwindow.close()
        self.main_menu.mainwindow.show()

    def toSearchPage(self):
        self.search_menu = SearchMenu(self.username, self.conn)
        self.search_menu.backButton.clicked.connect(self.backFromSearch)

        self.main_menu.mainwindow.close()
        self.search_menu.searchwindow.show()

    def backFromSearch(self):
        self.search_menu.searchwindow.close()
        self.main_menu.mainwindow.show()

    def toStatementPage(self):
        self.statement_menu = StatementMenu(self.username, self.conn)
        self.statement_menu.backButton.clicked.connect(self.backFromStatement)

        self.main_menu.mainwindow.close()
        self.statement_menu.statementwindow.show()

    def backFromStatement(self):
        self.statement_menu.statementwindow.close()
        self.main_menu.mainwindow.show()


if __name__ == '__main__':
    app = QApplication([])

    stats = Main()

    app.exec_()

