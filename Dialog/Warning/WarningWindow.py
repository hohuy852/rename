from PyQt5.QtWidgets import QDialog
from Dialog.Warning.Warning import Warning_Dialog
from PyQt5.QtCore import Qt

class WarningDialog(QDialog):
    def __init__(self, parent=None):
        super(WarningDialog, self).__init__(parent)
        self.ui = Warning_Dialog()
        self.setFixedSize(421, 269)
        self.ui.setupUi(self)
        self.log = self.ui.textBrowser
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)

    def show_message(self, message):
        self.log.append(message)
        self.exec_()
