from PyQt5.QtWidgets import QDialog
from Dialog.Renaming.Rename import Rename_Dialog
from PyQt5.QtCore import pyqtSignal, Qt

class RenameDialog(QDialog):
    confirm_signal = pyqtSignal(str)
    custom_signal = pyqtSignal()

    def __init__(self, parent=None):
        super(RenameDialog, self).__init__(parent)
        self.ui = Rename_Dialog()
        self.setFixedSize(399, 328)
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)

        self.confirm_btn = self.ui.confirm_btn
        self.cancel_btn = self.ui.cancel_btn
        self.newName = self.ui.newName

        # frame
        self.inputFrame = self.ui.frame_2
        # self.choicesFrame = self.ui.frame_5

        # radio
        self.custom = self.ui.custom
        self.ui.custom.setDefault(True)
        self.auto = self.ui.manual

        # Connect buttons to functions
        self.ui.confirm_btn.clicked.connect(self.confirm_action)
        self.ui.cancel_btn.clicked.connect(self.cancel_action)

        # Connect radio button toggled signal to show_hide_frame function
        self.auto.toggled.connect(self.show_hide_frame)

        self.show_hide_frame(False)

    def confirm_action(self):
        new_name = self.newName.text()
        if self.custom.isChecked():
            self.custom_signal.emit()
            self.close()
        elif self.auto.isChecked():
            if new_name:
                self.confirm_signal.emit(new_name)
                self.close()

    def cancel_action(self):
        self.close()

    def show_hide_frame(self, checked):
        self.inputFrame.setVisible(checked)
        # self.choicesFrame .setVisible(checked)
