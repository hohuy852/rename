from PyQt5.QtWidgets import QMainWindow,QDialog
from Rename import Rename_Dialog
from PyQt5.QtCore import pyqtSignal
        
class RenameDialog(QDialog):
    confirm_signal = pyqtSignal(str)
    def __init__(self):
        super(RenameDialog, self).__init__()
        self.ui = Rename_Dialog()
        self.setFixedSize(399, 328)
        self.ui.setupUi(self)

        self.confirm_btn = self.ui.confirm_btn
        self.cancel_btn = self.ui.cancel_btn
        self.newName = self.ui.newName

        self.custom = self.ui.custom
        self.auto = self.ui.manual
        # Connect buttons to functions
        self.ui.confirm_btn.clicked.connect(self.confirm_action)
        self.ui.cancel_btn.clicked.connect(self.cancel_action)

    def confirm_action(self):
        new_name = self.newName.text()
        if new_name:
            self.confirm_signal.emit(new_name)
            self.close()

    def cancel_action(self):
        self.close()
