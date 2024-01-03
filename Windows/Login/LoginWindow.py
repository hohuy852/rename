from PyQt5.QtWidgets import QDialog,QMainWindow
from Windows.Login.Login import Login_Window
from PyQt5.QtCore import pyqtSignal, Qt

class LoginWindow(QMainWindow):
    def __init__(self):
        super(LoginWindow, self).__init__()

        self.ui = Login_Window()
        self.ui.setupUi(self)
