from PyQt5.QtWidgets import QWidget
from Windows.Login.Login import Login_Form

class LoginForm(QWidget):
    def __init__(self):
        super(LoginForm, self).__init__()
        Form = QWidget
        ui = Login_Form()
        ui.setupUi(Form)
        Form.show()