from PyQt5.QtWidgets import QMainWindow, QFileDialog,QHeaderView,QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem
import os
import openpyxl
from App import Ui_MainWindow
from Dialog.Renaming.RenameWindow import RenameDialog

        
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Init Elements
        self.open_btn = self.ui.open_btn
        self.save_btn = self.ui.save_btn
        self.export_btn = self.ui.export_btn
        self.import_btn = self.ui.import_btn
        self.table_view = self.ui.tableView
        self.rename_btn = self.ui.rename_btn
        # Connect signals and slots
        self.open_btn.clicked.connect(self.show_folder_dialog)
        # self.save_btn.clicked.connect(self.rename_folders_excel)
        self.rename_btn.clicked.connect(self.show_rename_dialog)
        self.export_btn.clicked.connect(self.export_to_xlsx)
        self.import_btn.clicked.connect(self.import_xlsx)
        # Create a standard item model for the table view
        self.model = QStandardItemModel()
        self.table_view.setModel(self.model)

    def show_rename_dialog(self):
        if self.model.rowCount() == 0:
            # Show a warning message
            QMessageBox.warning(self, "Warning", "No data in the table to rename.")
            return
        dialog = RenameDialog(self)
        dialog.confirm_signal.connect(self.rename_folders)
        dialog.custom_signal.connect(self.rename_folders_excel)
        dialog.exec_()

    def show_folder_dialog(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Select Directory")
        if folder_path:
            self.load_folder_contents(folder_path)

    def load_folder_contents(self, folder_path):
        # Clear existing items from the model
        self.model.clear()

        # Set up table headers
        self.model.setHorizontalHeaderLabels(["Path", "Name", "New Name"])
        
        # Set header width to 33% for each column
        header = self.table_view.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)  # Path column takes the remaining space
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)  # Name column adjusts to content
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)  # New Name column adjusts to content
        # Recursively iterate through the folder contents
        self.add_folders_to_model(folder_path)

    def add_folders_to_model(self, folder_path):
        for root, dirs, files in os.walk(folder_path):
            for name in dirs:
                item = QStandardItem(name)
                item_path = os.path.normpath(os.path.join(root, name))
                item.setData(item_path, Qt.UserRole + 1)  # Save path in UserRole+1
                self.model.appendRow([QStandardItem(item_path), item])
                
    def load_files(self, folder_path):
        self.model.clear()

        # Set up table headers
        self.model.setHorizontalHeaderLabels(["Path", "Name", "New Name"])

        # Set header width to 50% for each column
        header = self.table_view.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)  # File Name column takes the remaining space
        header.setSectionResizeMode(1, QHeaderView.Stretch)  # File Path column takes the remaining space
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)  # New Name column adjusts to content

        # Add files to the model
        self.add_files_to_model(folder_path)

    def add_files_to_model(self, folder_path):
        for root, dirs, files in os.walk(folder_path):
            for file_name in files:
                file_path = os.path.join(root, file_name)

                # Create QStandardItems for file name and file path
                file_name_item = QStandardItem(file_name)
                file_path_item = QStandardItem(file_path)

                # Set data for file path in UserRole + 1
                file_path_item.setData(file_path, Qt.UserRole + 1)

                # Append the items to the model
                self.model.appendRow([file_path_item, file_name_item])

    def rename_folders(self,new_name):
        items = self.get_sorted_items_by_depth()
        
        index = 1  # Initialize an index to make the new name unique
        
        for item in items:
            old_path = item.data(Qt.UserRole + 1)
            new_path = os.path.join(os.path.dirname(old_path), f"{new_name}_{index}")
            
            # Check if the new path already exists, and increment the index if needed
            while os.path.exists(new_path):
                index += 1
                new_path = os.path.join(os.path.dirname(old_path), f"{new_name}_{index}")

            os.rename(old_path, new_path)
            item.setData(new_path, Qt.UserRole + 1)
            item.setText(f"{new_name}_{index}")

    def rename_folders_excel(self):
        items = self.get_sorted_items_by_depth()

        for row in range(len(items)):
            name_item = self.model.item(row, 0)
            path_item = self.model.item(row, 1)
            new_name_item = self.model.item(row, 2)

            old_path = path_item.data(Qt.UserRole + 1)
            new_name = new_name_item.text()

            # Check if the old path exists
            if os.path.exists(old_path):
                # Skip if the "New Name" column has the same value
                if new_name and new_name != name_item.text():
                    new_path = os.path.join(os.path.dirname(old_path), new_name)

                    # Check if the new path already exists
                    if os.path.exists(new_path):
                        print(f"Skipping rename for path '{old_path}' as '{new_name}' already exists")
                    else:
                        try:
                            # Rename the folder
                            os.rename(old_path, new_path)

                            # Update the model data
                            path_item.setData(new_path, Qt.UserRole + 1)
                            name_item.setText(new_name)
                        except FileExistsError:
                            print(f"Error renaming '{old_path}' to '{new_path}': File already exists")
                elif not new_name:
                    print(f"New Name not provided for path: {old_path}")
                else:
                    print(f"Skipping rename for path '{old_path}' as 'New Name' is the same")
            else:
                print(f"Folder does not exist: {old_path}. Skipping.")


    def get_sorted_items_by_depth(self):
        items = []
        for row in range(self.model.rowCount()):
            item = self.model.item(row, 1)
            items.append(item)
        items.sort(key=lambda x: x.data(Qt.UserRole + 1).count(os.sep), reverse=True)
        return items
    
    def export_to_xlsx(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Save Excel File", "", "Excel Files (*.xlsx)")

        if file_path:
            # Create a new Excel workbook and select the active sheet
            workbook = openpyxl.Workbook()
            sheet = workbook.active

            # Write headers to the Excel file
            headers = ["Path", "Name", "New Name"]
            
            for col_num, header in enumerate(headers, 1):
                sheet.cell(row=1, column=col_num, value=header)

            # Write data to the Excel file
            for row in range(self.model.rowCount()):
                name_item = self.model.item(row, 0)
                path_item = self.model.item(row, 1)
                
                name_value = name_item.text()
                path_value = path_item.text()
                new_value  = ""

                sheet.append([name_value, path_value, new_value])

            # Save the Excel file
            workbook.save(file_path)

    def import_xlsx(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Excel File", "", "Excel Files (*.xlsx)")
        if file_path:
            workbook = openpyxl.load_workbook(file_path)
            sheet = workbook.active

            headers = [cell.value for cell in sheet[1]]

            self.model.clear()

            self.model.setHorizontalHeaderLabels(headers)

            items = []
            for row in sheet.iter_rows(min_row=2, values_only=True):
                new_name_value = row[2] if row[2] is not None else ""

                # Set the data for the new item
                path_item = QStandardItem(str(row[0]))
                path_item.setData(str(row[0]), Qt.UserRole + 1)  # Set the path in UserRole+1
                items.append(path_item)

                row_items = [
                    QStandardItem(str(row[0])),  # "Path" column
                    path_item,  # "Name" column
                    QStandardItem(str(new_name_value))  # "New Name" column
                ]
                self.model.appendRow(row_items)

            # Set header width to 33% for each column
            header = self.table_view.horizontalHeader()
            header.setSectionResizeMode(0, QHeaderView.Stretch)  # Path column takes the remaining space
            header.setSectionResizeMode(1, QHeaderView.ResizeToContents)  # Name column adjusts to content
            header.setSectionResizeMode(2, QHeaderView.ResizeToContents)  # New Name column adjusts to content

            # No sorting here

            workbook.close()
