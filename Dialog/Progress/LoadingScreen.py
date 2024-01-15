from PyQt5.QtWidgets import QDialog
from Dialog.Progress.ProgressBar import ProgressBar
from PyQt5.QtCore import pyqtSignal, Qt

class LoadingScreen(QDialog):
    def __init__(self, parent=None):
        super(LoadingScreen, self).__init__(parent)
        self.ui = ProgressBar()
        self.setFixedSize(323, 72)
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)
        self.loadingBar = self.ui.progressBar