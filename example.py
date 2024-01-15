import sys
from PyQt5.QtCore import Qt, QThread, pyqtSignal, QObject
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QPushButton, QWidget


# Worker class
class Worker(QObject):
    finished = pyqtSignal()

    def do_work(self):
        # Simulate some time-consuming task
        for i in range(5):
            print(f"Working on thread 1")
            QThread.msleep(1000)  # Sleep for 1 second
        # Emit signal when work is done
        self.finished.emit()


# Main window class
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.worker_thread = QThread()
        self.worker = Worker()

        self.init_ui()

    def init_ui(self):
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)

        self.label = QLabel("Click the button to start work")
        layout.addWidget(self.label)

        self.button = QPushButton("Start Work")
        self.button.clicked.connect(self.start_work)
        layout.addWidget(self.button)

        self.setCentralWidget(central_widget)

        # Move the worker object to the worker thread
        self.worker.moveToThread(self.worker_thread)

        # Connect signals and slots
        self.worker_thread.started.connect(self.worker.do_work)
        self.worker.finished.connect(self.worker_thread.quit)
        self.worker_thread.finished.connect(self.worker.deleteLater)

    def start_work(self):
        self.label.setText("Work in progress...")
        self.worker_thread.start()
        self.worker_thread.finished.connect(self.work_finished)

    def work_finished(self):
        self.label.setText("Work done.")
        self.worker_thread.finished.disconnect(self.work_finished)
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
