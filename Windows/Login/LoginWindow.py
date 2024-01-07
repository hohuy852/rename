from PyQt5.QtWidgets import QDialog,QMainWindow,QMessageBox
from Windows.Login.Login import Login_Window
from PyQt5.QtCore import pyqtSignal, Qt
from mainwindow import MainWindow
from dotenv import load_dotenv
import json
import requests, os
load_dotenv()

class LoginWindow(QMainWindow):
    def __init__(self):
        super(LoginWindow, self).__init__()

        self.ui = Login_Window()
        self.ui.setupUi(self)
        self.closeBtn = self.ui.closeBtn
        self.loginBtn = self.ui.loginBtn
        self.username = self.ui.username
        self.password = self.ui.password
        self.closeBtn.clicked.connect(self.closeWindow)
        self.loginBtn.clicked.connect(self.login)
        self.mainwindow = None

    def validateAndLogin(self):
        username = self.username.text()
        password = self.password.text()

        if not username or not password:
            QMessageBox.warning(self, "Validation Error", "Username and password are required.")
            return


    def closeWindow(self):
        self.close()

    def login(self):
        username = self.username.text()
        password = self.password.text()
        # Make API call
        api_url = os.getenv("API_URL")
        data = {'username': username, 'password': password}
        headers = {
            "Content-Type": "application/json"
        }
        try:
            response = requests.post(api_url,  data=json.dumps(data), headers=headers)
            parsed_response = json.loads(response.text)
            if 'statusCode' in parsed_response and parsed_response['statusCode'] == 200:

                self.close()

                # Show the MainWindow only if it's not already created
                if not self.mainwindow:
                    self.mainwindow = MainWindow()
                    self.mainwindow.show()

            else:
                # Handle unsuccessful login (e.g., show an error message)
                QMessageBox.warning(self, "Warning", "login fail.")
                print(f"Login failed. Status code: {response}")
        except Exception as e:
            # Handle exceptions (e.g., network error)
            QMessageBox.warning(self, "Warning", "error.")
            print(f"Error during login: {str(e)}")


