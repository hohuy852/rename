# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'rename.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QTableView,
    QVBoxLayout, QWidget)
import assets_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 750)
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        icon = QIcon()
        icon.addFile(u":/icons/resource/icons8-open-file-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionOpen.setIcon(icon)
        self.actionOpen.setIconVisibleInMenu(False)
        self.actionsave = QAction(MainWindow)
        self.actionsave.setObjectName(u"actionsave")
        icon1 = QIcon()
        icon1.addFile(u":/icons/resource/icons8-save-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionsave.setIcon(icon1)
        self.actionsave.setIconVisibleInMenu(False)
        self.actionSave_As = QAction(MainWindow)
        self.actionSave_As.setObjectName(u"actionSave_As")
        self.actionExport = QAction(MainWindow)
        self.actionExport.setObjectName(u"actionExport")
        icon2 = QIcon()
        icon2.addFile(u":/icons/resource/icons8-export-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionExport.setIcon(icon2)
        self.actionExport.setIconVisibleInMenu(False)
        self.actionImport = QAction(MainWindow)
        self.actionImport.setObjectName(u"actionImport")
        icon3 = QIcon()
        icon3.addFile(u":/icons/resource/icons8-import-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionImport.setIcon(icon3)
        self.actionImport.setIconVisibleInMenu(False)
        self.actionRename = QAction(MainWindow)
        self.actionRename.setObjectName(u"actionRename")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tools = QFrame(self.centralwidget)
        self.tools.setObjectName(u"tools")
        self.tools.setMinimumSize(QSize(0, 92))
        self.tools.setMaximumSize(QSize(16777215, 92))
        self.tools.setStyleSheet(u"background-color: rgb(195, 195, 195);")
        self.tools.setFrameShape(QFrame.StyledPanel)
        self.tools.setFrameShadow(QFrame.Raised)
        self.verticalLayoutWidget = QWidget(self.tools)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 0, 52, 91))
        self.open_layout = QVBoxLayout(self.verticalLayoutWidget)
        self.open_layout.setObjectName(u"open_layout")
        self.open_layout.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.open_layout.addItem(self.verticalSpacer)

        self.open_btn = QPushButton(self.verticalLayoutWidget)
        self.open_btn.setObjectName(u"open_btn")
        self.open_btn.setMinimumSize(QSize(50, 50))
        self.open_btn.setMaximumSize(QSize(60, 60))
        self.open_btn.setIcon(icon)

        self.open_layout.addWidget(self.open_btn)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.open_layout.addItem(self.verticalSpacer_2)

        self.verticalLayoutWidget_2 = QWidget(self.tools)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(80, 0, 52, 91))
        self.save_layout = QVBoxLayout(self.verticalLayoutWidget_2)
        self.save_layout.setObjectName(u"save_layout")
        self.save_layout.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.save_layout.addItem(self.verticalSpacer_3)

        self.save_btn = QPushButton(self.verticalLayoutWidget_2)
        self.save_btn.setObjectName(u"save_btn")
        self.save_btn.setMinimumSize(QSize(50, 50))
        self.save_btn.setMaximumSize(QSize(60, 60))
        self.save_btn.setIcon(icon1)

        self.save_layout.addWidget(self.save_btn)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.save_layout.addItem(self.verticalSpacer_4)

        self.verticalLayoutWidget_3 = QWidget(self.tools)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(1040, 0, 52, 91))
        self.import_layout = QVBoxLayout(self.verticalLayoutWidget_3)
        self.import_layout.setObjectName(u"import_layout")
        self.import_layout.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.import_layout.addItem(self.verticalSpacer_5)

        self.import_btn = QPushButton(self.verticalLayoutWidget_3)
        self.import_btn.setObjectName(u"import_btn")
        self.import_btn.setMinimumSize(QSize(50, 50))
        self.import_btn.setMaximumSize(QSize(60, 60))
        self.import_btn.setIcon(icon3)

        self.import_layout.addWidget(self.import_btn)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.import_layout.addItem(self.verticalSpacer_6)

        self.verticalLayoutWidget_4 = QWidget(self.tools)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(1110, 0, 52, 91))
        self.export_layout = QVBoxLayout(self.verticalLayoutWidget_4)
        self.export_layout.setObjectName(u"export_layout")
        self.export_layout.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.export_layout.addItem(self.verticalSpacer_7)

        self.export_btn = QPushButton(self.verticalLayoutWidget_4)
        self.export_btn.setObjectName(u"export_btn")
        self.export_btn.setMinimumSize(QSize(50, 50))
        self.export_btn.setMaximumSize(QSize(60, 60))
        self.export_btn.setIcon(icon2)

        self.export_layout.addWidget(self.export_btn)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.export_layout.addItem(self.verticalSpacer_8)

        self.verticalLayoutWidget_5 = QWidget(self.tools)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(140, 0, 52, 91))
        self.rename_layout = QVBoxLayout(self.verticalLayoutWidget_5)
        self.rename_layout.setObjectName(u"rename_layout")
        self.rename_layout.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.rename_layout.addItem(self.verticalSpacer_9)

        self.rename_btn = QPushButton(self.verticalLayoutWidget_5)
        self.rename_btn.setObjectName(u"rename_btn")
        self.rename_btn.setMinimumSize(QSize(50, 50))
        self.rename_btn.setMaximumSize(QSize(60, 60))
        icon4 = QIcon()
        icon4.addFile(u":/icons/resource/icons8-rename-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.rename_btn.setIcon(icon4)

        self.rename_layout.addWidget(self.rename_btn)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.rename_layout.addItem(self.verticalSpacer_10)


        self.verticalLayout_2.addWidget(self.tools)

        self.content = QFrame(self.centralwidget)
        self.content.setObjectName(u"content")
        self.content.setMaximumSize(QSize(16777215, 16777215))
        self.content.setStyleSheet(u"background-color: rgb(204, 204, 204);")
        self.content.setFrameShape(QFrame.StyledPanel)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.content)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.leftSide = QFrame(self.content)
        self.leftSide.setObjectName(u"leftSide")
        self.leftSide.setMaximumSize(QSize(16777215, 16777215))
        self.leftSide.setFrameShape(QFrame.StyledPanel)
        self.leftSide.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftSide)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tableView = QTableView(self.leftSide)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout_3.addWidget(self.tableView)


        self.horizontalLayout.addWidget(self.leftSide)


        self.verticalLayout_2.addWidget(self.content)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1200, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuAction = QMenu(self.menubar)
        self.menuAction.setObjectName(u"menuAction")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAction.menuAction())
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionsave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuAction.addAction(self.actionExport)
        self.menuAction.addAction(self.actionImport)
        self.menuAction.addAction(self.actionRename)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionsave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.actionSave_As.setText(QCoreApplication.translate("MainWindow", u"Save As", None))
        self.actionExport.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.actionImport.setText(QCoreApplication.translate("MainWindow", u"Import", None))
        self.actionRename.setText(QCoreApplication.translate("MainWindow", u"Rename", None))
        self.open_btn.setText("")
        self.save_btn.setText("")
        self.import_btn.setText("")
        self.export_btn.setText("")
        self.rename_btn.setText("")
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuAction.setTitle(QCoreApplication.translate("MainWindow", u"Actions", None))
    # retranslateUi

