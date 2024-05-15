from PyQt5.QtWidgets import QDialog, QMainWindow, QMessageBox, QApplication
from Windows.Login.Login import Login_Window
from PyQt5.QtCore import pyqtSignal, Qt
from mainwindow import MainWindow
from dotenv import load_dotenv
import json
import requests, os
from cryptography.fernet import Fernet

load_dotenv()
CREDENTIALS_FILE = "credentials.json"
KEY_FILE = 'secret.key'

class LoginWindow(QMainWindow):
    username_signal = pyqtSignal(str)

    def __init__(self):
        super(LoginWindow, self).__init__()
        self.ui = Login_Window()
        self.setFixedSize(612, 617)
        self.ui.setupUi(self)
        self.closeBtn = self.ui.closeBtn
        self.loginBtn = self.ui.loginBtn
        self.username = self.ui.username
        self.password = self.ui.password
        self.warning = self.ui.warning
        self.closeBtn.clicked.connect(self.closeWindow)
        self.loginBtn.clicked.connect(self.login)
        self.mainwindow = None
        self.remember = self.ui.remember

        self.key = self.load_or_generate_key()
        self.fernet = Fernet(self.key)
        
        # Load saved credentials if available
        self.load_credentials()

    def closeWindow(self):
        self.close()

    def keyPressEvent(self, event):
        # Check if the pressed key is Enter (Return)
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            # Check if both username and password fields are non-empty
            if self.username.text() and self.password.text():
                # Call the login method when Enter key is pressed and both fields are non-empty
                self.login()

    def login(self):
        username = self.username.text()
        password = self.password.text()

        # Make API call
        api_url = (
            "https://k02nwn2ep7.execute-api.ap-northeast-1.amazonaws.com/dev/login/"
        )
        data = {"username": username, "password": password}

        headers = {"Content-Type": "application/json"}

        if not username or not password:
            self.warning.setText("Missing username or password")
            return
        try:
            self.loginBtn.setText("Logging in...")
            QApplication.processEvents()
            response = requests.post(api_url, data=json.dumps(data), headers=headers)
            parsed_response = json.loads(response.text)
            if "statusCode" in parsed_response and parsed_response["statusCode"] == 200:
                body = json.loads(parsed_response["body"])
                logged_username = body.get("username", None)
                if self.remember.isChecked():
                    self.save_credentials(username, password)
                self.close()
                # Show the MainWindow only if it's not already created
                if not self.mainwindow:
                    self.mainwindow = MainWindow(logged_username)
                    self.mainwindow.show()

            else:
                # Handle unsuccessful login (e.g., show an error message)
                self.warning.setText("Wrong username or password")
                print(f"Login failed. Status code: {response}")
        except Exception as e:
            # Handle exceptions (e.g., network error)
            self.warning.setText("An error occur !")
            print(f"Error during login: {str(e)}")
        finally:
            self.loginBtn.setText("Log In")

    def save_credentials(self, username, password):
        credentials = {
            "username": self.fernet.encrypt(username.encode()).decode(),
            "password": self.fernet.encrypt(password.encode()).decode(),
        }
        with open(CREDENTIALS_FILE, "w") as file:
            json.dump(credentials, file)

    def load_credentials(self):
        if os.path.exists(CREDENTIALS_FILE):
            with open(CREDENTIALS_FILE, 'r') as file:
                credentials = json.load(file)
                username = self.fernet.decrypt(credentials['username'].encode()).decode()
                password = self.fernet.decrypt(credentials['password'].encode()).decode()
                self.username.setText(username)
                self.password.setText(password)
                self.remember.setChecked(True)

    def clear_credentials(self):
        if os.path.exists(CREDENTIALS_FILE):
            os.remove(CREDENTIALS_FILE)
    
    def load_or_generate_key(self):
        if os.path.exists(KEY_FILE):
            with open(KEY_FILE, 'rb') as file:
                key = file.read()
        else:
            key = Fernet.generate_key()
            with open(KEY_FILE, 'wb') as file:
                file.write(key)
        return key
