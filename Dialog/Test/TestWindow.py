from PyQt5.QtWidgets import QDialog
from Dialog.Test.Test import Test_Dialog
from PyQt5.QtCore import Qt

class TestDialog(QDialog):
    def __init__(self, parent=None):
        super(TestDialog, self).__init__(parent)
        self.ui = Test_Dialog()
        self.setFixedSize(316, 87)
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)
