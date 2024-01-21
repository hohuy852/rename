from PyQt5.QtWidgets import QDialog
from Dialog.Select.TypeSelect import Type_Dialog
from PyQt5.QtCore import pyqtSignal, Qt


class TypeDialog(QDialog):
    folder_signal = pyqtSignal()
    file_signal = pyqtSignal()

    def __init__(self, parent=None):
        super(TypeDialog, self).__init__(parent)
        self.ui = Type_Dialog()
        self.ui.setupUi(self)
        self.folder = self.ui.open_folder
        self.file = self.ui.open_file
        self.folder.clicked.connect(self.folderSelect)
        self.file.clicked.connect(self.fileSelect)
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)

    def folderSelect(self):
        self.folder_signal.emit()

    def fileSelect(self):
        self.file_signal.emit()
