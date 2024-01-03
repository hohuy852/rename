import sys
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore
from Windows.Login.LoginWindow import LoginWindow
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    window.setAttribute(QtCore.Qt.WA_TranslucentBackground)
    window.show()
    sys.exit(app.exec_())
