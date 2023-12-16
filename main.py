from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
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

    def logining(self):
        self.username = self.login_menu.usernameInput.text()
        self.password = self.login_menu.passwordInput.text()
        self.main_menu = MainMenu(self.username)
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
        self.account_menu = AccountMenu(self.username)
        self.account_menu.backButton.clicked.connect(self.backFromAccount)

        self.main_menu.mainwindow.close()
        self.account_menu.accountwindow.show()

    def backFromAccount(self):
        self.account_menu.accountwindow.close()
        self.main_menu.mainwindow.show()

    def toSearchPage(self):
        self.search_menu = SearchMenu(self.username)
        self.search_menu.backButton.clicked.connect(self.backFromSearch)

        self.main_menu.mainwindow.close()
        self.search_menu.searchwindow.show()

    def backFromSearch(self):
        self.search_menu.searchwindow.close()
        self.main_menu.mainwindow.show()

    def toStatementPage(self):
        self.statement_menu = StatementMenu(self.username)
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

