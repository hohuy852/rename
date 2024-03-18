from PyQt5.QtWidgets import QDialog ,QMessageBox, QFileSystemModel
from Dialog.Filter.Filter import Filter_Dialog
from PyQt5.QtCore import pyqtSignal, Qt, QDir


class FilterDialog(QDialog):
    def __init__(self, parent=None):
        super(FilterDialog, self).__init__(parent)
        self.ui = Filter_Dialog()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)
        self.tree = self.ui.treeView
        
        # Create a file system model
        self.model = QFileSystemModel()
        
        # Use a demo path instead of the entire file system
        demo_path = "D:/"  # Assuming D drive is available
        self.model.setRootPath(demo_path)
        self.model.setRootPath(demo_path)
        
        self.tree.setModel(self.model)

        # Set root index to the demo path
        self.tree.setRootIndex(self.model.index(demo_path))
        
        # Enable sorting
        self.tree.setSortingEnabled(True)
        
        # Hide unnecessary columns
        self.tree.hideColumn(1)  # Hide size column
        self.tree.hideColumn(2)  # Hide type column
        self.tree.hideColumn(3)  # Hide date modified colum