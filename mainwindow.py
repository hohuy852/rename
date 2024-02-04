import os
import openpyxl
from PyQt5.QtWidgets import (
    QMainWindow,
    QFileDialog,
    QHeaderView,
    QMessageBox,
    QApplication,
)
from PyQt5.QtCore import Qt, pyqtSignal, QThread
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from App2 import Ui_MainWindow
from Dialog.Renaming.RenameWindow import RenameDialog
from Dialog.Progress.LoadingScreen import LoadingScreen
from Dialog.Select.SelectWindow import TypeDialog
from pathlib import Path


class LoadFilesThread(QThread):
    progress_updated = pyqtSignal(int)  # Signal to update the progress bar
    loading_completed = pyqtSignal()

    def __init__(self, folder_path):
        super(LoadFilesThread, self).__init__()
        self.folder_path = folder_path

    def run(self):
        total_files = sum(len(files) for _, _, files in os.walk(self.folder_path))
        loaded_files = 0

        for root, dirs, files in os.walk(self.folder_path):
            for file_name in files:
                file_path = os.path.join(root, file_name)

                # Create QStandardItems for file name and file path
                file_name_item = QStandardItem(file_name)
                file_path_item = QStandardItem(file_path)

                # Set data for file path in UserRole + 1
                file_path_item.setData(file_path, Qt.UserRole + 1)

                # Append the items to the model
                self.model.appendRow([file_path_item, file_name_item])

                # Update progress
                loaded_files += 1
                percent = loaded_files / total_files * 100
                self.progress_updated.emit(int(percent))

        self.loading_completed.emit()


class MainWindow(QMainWindow):
    def __init__(self, logged_username):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.loading = LoadingScreen(self)
        self.selectDialog = TypeDialog(self)
        # Init Elements
        self.open_btn = self.ui.open_btn
        # self.save_btn = self.ui.save_btn
        self.export_btn = self.ui.export_btn
        self.import_btn = self.ui.import_btn
        self.table_view = self.ui.tableView
        self.username = self.ui.name
        self.rename_btn = self.ui.rename_btn
        # Connect signals and slots
        self.open_btn.clicked.connect(self.show_type_dialog)
        # self.save_btn.clicked.connect(self.rename_folders_excel)
        self.rename_btn.clicked.connect(self.show_rename_dialog)
        self.export_btn.clicked.connect(self.export_to_xlsx)
        self.import_btn.clicked.connect(self.import_xlsx)
        # Create a standard item model for the table view
        self.model = QStandardItemModel()
        self.table_view.setModel(self.model)
        self.username.setText(logged_username)
        self.folder_signal_connected = False
        self.file_signal_connected = False

    def show_rename_dialog(self):
        if self.model.rowCount() == 0:
            # Show a warning message
            QMessageBox.warning(self, "Warning", "No data in the table to rename.")
            return
        dialog = RenameDialog(self)
        dialog.confirm_signal.connect(self.rename_folders)
        dialog.custom_signal.connect(self.rename_folders_excel)
        dialog.exec_()

    def show_file_dialog(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Select Directory")
        if folder_path:
            self.load_files(folder_path)
        self.selectDialog.hide()

    def show_folder_dialog(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Select Directory")
        if folder_path:
            self.load_folder_contents(folder_path)
        self.selectDialog.hide()

    def show_type_dialog(self):
        # Disconnect signals if they are connected
        if self.folder_signal_connected:
            self.selectDialog.folder_signal.disconnect(self.show_folder_dialog)
            self.folder_signal_connected = False

        if self.file_signal_connected:
            self.selectDialog.file_signal.disconnect(self.show_file_dialog)
            self.file_signal_connected = False

        # Connect signals to slots if they are not connected
        if not self.folder_signal_connected:
            self.selectDialog.folder_signal.connect(self.show_folder_dialog)
            self.folder_signal_connected = True

        if not self.file_signal_connected:
            self.selectDialog.file_signal.connect(self.show_file_dialog)
            self.file_signal_connected = True

        # Show the dialog
        self.selectDialog.exec_()

    def load_folder_contents(self, folder_path):
        # Clear existing items from the model
        self.model.clear()

        # Set up table headers
        self.model.setHorizontalHeaderLabels(["Path", "Name", "New Name"])

        # Set header width to 33% for each column
        header = self.table_view.horizontalHeader()
        header.setSectionResizeMode(
            0, QHeaderView.Stretch
        )  # Path column takes the remaining space
        header.setSectionResizeMode(
            1, QHeaderView.ResizeToContents
        )  # Name column adjusts to content
        header.setSectionResizeMode(
            2, QHeaderView.ResizeToContents
        )  # New Name column adjusts to content
        # Recursively iterate through the folder contents
        self.add_folders_to_model(folder_path)

    def add_folders_to_model(self, folder_path):
        for root, dirs, files in os.walk(folder_path):
            for name in dirs:
                item = QStandardItem(name)
                item_path = os.path.normpath(os.path.join(root, name))
                item.setData(item_path, Qt.UserRole + 1)  # Save path in UserRole+1
                self.model.appendRow([QStandardItem(item_path), item])

    def print_table_data(self):
        for row in range(self.model.rowCount()):
            for col in range(self.model.columnCount()):
                item = self.model.item(row, col)
                if item is not None:
                    item_data = item.data()
                    print(f"Row {row}, Column {col}: {item_data}")
                else:
                    print(f"Row {row}, Column {col}: None")

    def load_files(self, folder_path):
        self.model.clear()
        # Set up table headers
        self.model.setHorizontalHeaderLabels(["Path", "Name", "New Name"])

        # Set header width to 50% for each column
        header = self.table_view.horizontalHeader()
        header.setSectionResizeMode(
            0, QHeaderView.Stretch
        )  # File Name column takes the remaining space
        header.setSectionResizeMode(
            1, QHeaderView.ResizeToContents
        )  # File Path column takes the remaining space
        header.setSectionResizeMode(
            2, QHeaderView.ResizeToContents
        )  # New Name column adjusts to content

        # Create and start the thread
        self.load_files_thread = LoadFilesThread(folder_path)
        self.load_files_thread.model = self.model
        self.loading.show()
        self.load_files_thread.progress_updated.connect(
            self.loading.loadingBar.setValue
        )
        self.load_files_thread.loading_completed.connect(self.loading_completed)
        self.load_files_thread.start()

        # Add files to the model
        # self.add_files_to_model(folder_path)

    def loading_completed(self):
        self.loading.loadingBar.setValue(0)
        self.loading.hide()

    def rename_folders(self, new_name):
        items = self.get_sorted_items_by_depth()

        index = 1  # Initialize an index to make the new name unique

        for item in items:
            old_path = item.data(Qt.UserRole + 1)
            new_path = os.path.join(os.path.dirname(old_path), f"{new_name}_{index}")

            # Check if the new path already exists, and increment the index if needed
            while os.path.exists(new_path):
                index += 1
                new_path = os.path.join(
                    os.path.dirname(old_path), f"{new_name}_{index}"
                )

            os.rename(old_path, new_path)
            item.setData(new_path, Qt.UserRole + 1)
            item.setText(f"{new_name}_{index}")

    def rename_folders_excel(self):
        error_log = []  # Create an empty list to store errors

        if all(
            self.model.item(row, 2) is None or self.model.item(row, 2).text() == ""
            for row in range(self.model.rowCount())
        ):
            # Show a warning if no values in the "New Name" column
            QMessageBox.warning(self, "Warning", "No 'New Name' values provided.")
            return

        # Sort items by depth in descending order
        items = self.get_sorted_items_by_depth()

        for item in items:
            row = self.model.findItems(item.text(), Qt.MatchExactly, 1)[0].row()
            name_item = self.model.item(row, 1)
            path_item = self.model.item(row, 0)
            new_name_item = self.model.item(row, 2)

            old_path = path_item.data(Qt.UserRole + 1) if path_item and path_item.data(Qt.UserRole + 1) else None

            # Check if the "New Name" item exists and has a value
            if new_name_item and new_name_item.text() != "" and old_path:
                new_name = new_name_item.text()

                # Check if the old path exists
                if os.path.exists(old_path):
                    # Check if the new path already exists
                    new_path = os.path.join(os.path.dirname(old_path), new_name)
                    if os.path.exists(new_path):
                        error_log.append(
                            {
                                "path": old_path,
                                "error": f"Skipping rename for path '{old_path}' as '{new_name}' already exists",
                            }
                        )
                    else:
                        try:
                            # Rename the folder
                            os.rename(old_path, new_path)

                            # Update the model data
                            path_item.setData(new_path, Qt.UserRole + 1)
                            name_item.setText(new_name)
                        except FileExistsError:
                            error_log.append(
                                {
                                    "path": old_path,
                                    "error": f"Error renaming '{old_path}' to '{new_path}': File already exists",
                                }
                            )
                else:
                    error_log.append(
                        {
                            "path": old_path,
                            "error": f"Folder does not exist: {old_path}.",
                        }
                    )
            else:
                error_log.append(
                    {
                        "path": old_path,
                        "error": f"Skipping rename for path '{old_path}' as 'New Name' is not provided",
                    }
                )

        # Export error log to Excel
        self.export_error_log_to_excel(error_log)


    def export_error_log_to_excel(self, error_log):
        if not error_log:
            print("No errors to export.")
            return

        desktop_path = str(Path.home() / "Desktop")
        file_path = os.path.join(desktop_path, "error_log.xlsx")

        # Create a new Excel workbook and select the active sheet
        workbook = openpyxl.Workbook()
        sheet = workbook.active

        # Write headers to the Excel file
        headers = ["path", "error"]
        for col_num, header in enumerate(headers, 1):
            sheet.cell(row=1, column=col_num, value=header)

        # Write data to the Excel file
        for row_num, error_entry in enumerate(error_log, 2):
            sheet.cell(row=row_num, column=1, value=error_entry["path"])
            sheet.cell(row=row_num, column=2, value=error_entry["error"])

        # Save the Excel file
        workbook.save(file_path)
        print(f"Error log saved to: {file_path}")

    def get_sorted_items_by_depth(self):
        items = []
        for row in range(self.model.rowCount()):
            item = self.model.item(row, 1)
            items.append(item)

        # Modify the sorting key function to handle None values
        items.sort(
            key=lambda x: (
                x.data(Qt.UserRole + 1).count(os.sep)
                if x and x.data(Qt.UserRole + 1)
                else 0
            ),
            reverse=True,
        )

        return items

    def export_to_xlsx(self):
        file_path, _ = QFileDialog.getSaveFileName(
            self, "Save Excel File", "", "Excel Files (*.xlsx)"
        )

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
                new_value = ""

                sheet.append([name_value, path_value, new_value])

            # Save the Excel file
            workbook.save(file_path)

    def import_xlsx(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Open Excel File", "", "Excel Files (*.xlsx)"
        )
        if file_path:
            workbook = openpyxl.load_workbook(file_path)
            sheet = workbook.active

            headers = [cell.value for cell in sheet[1]]

            self.model.clear()

            if headers:
                self.model.setHorizontalHeaderLabels(headers)

                for row in sheet.iter_rows(min_row=2, values_only=True):
                    new_name_value = row[2] if row[2] is not None else ""

                    # Set the data for the new item
                    path_item = QStandardItem(str(row[0]))
                    path_item.setData(
                        str(row[0]), Qt.UserRole + 1
                    )  # Set the path in UserRole+1

                    name_item = QStandardItem(str(row[1]))
                    row_items = [
                        path_item,  # "Path" column
                        name_item,  # "Name" column
                        QStandardItem(str(new_name_value)),  # "New Name" column
                    ]
                    self.model.appendRow(row_items)

                # Set header width to 33% for each column
                header = self.table_view.horizontalHeader()
                header.setSectionResizeMode(
                    0, QHeaderView.Stretch
                )  # Path column takes the remaining space
                header.setSectionResizeMode(
                    1, QHeaderView.ResizeToContents
                )  # Name column adjusts to content
                header.setSectionResizeMode(
                    2, QHeaderView.ResizeToContents
                )  # New Name column adjusts to content

                workbook.close()