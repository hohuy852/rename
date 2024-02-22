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

        
    def create_test(self):
        self.root_dir = "TestParent"
        self.child_dirs = ["TestChild1", "TestChild2", "TestChild3", "TestChild4"]
        self.grandchild_dirs = ["TestChild5"]
        self.files = ["testfile.txt", "testfile1.txt", "testfile2.txt", "testfile3.txt", "testfile4.txt", "testfile5.txt"]