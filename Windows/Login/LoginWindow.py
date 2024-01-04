from PyQt5.QtWidgets import QDialog,QMainWindow
from Windows.Login.Login import Login_Window
from PyQt5.QtCore import pyqtSignal, Qt
from mainwindow import MainWindow
from dotenv import load_dotenv
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

    def closeWindow(self):
        self.close()

    def login(self):
        username = self.username.text()
        password = self.password.text()
        # Make API call
        api_url = os.getenv("API_URL")
        data = {'username': username, 'password': password}

        try:
            response = requests.post(api_url, json=data)

            if response.status_code == 200:
                # Successful login, emit a signal with user data
                user_data = response.json()  # Modify this based on your API response structure
                print("success")
            else:
                # Handle unsuccessful login (e.g., show an error message)
                print(f"Login failed. Status code: {response}")
        except Exception as e:
            # Handle exceptions (e.g., network error)
            print(f"Error during login: {str(e)}")


