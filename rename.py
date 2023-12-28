# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './rename.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 750)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tools = QtWidgets.QFrame(self.centralwidget)
        self.tools.setMinimumSize(QtCore.QSize(0, 92))
        self.tools.setMaximumSize(QtCore.QSize(16777215, 92))
        self.tools.setStyleSheet("background-color: rgb(195, 195, 195);")
        self.tools.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tools.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tools.setObjectName("tools")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tools)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 0, 52, 91))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.open_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.open_layout.setContentsMargins(0, 0, 0, 0)
        self.open_layout.setObjectName("open_layout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.open_layout.addItem(spacerItem)
        self.open_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.open_btn.setMinimumSize(QtCore.QSize(50, 50))
        self.open_btn.setMaximumSize(QtCore.QSize(60, 60))
        self.open_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/resource/icons8-open-file-50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.open_btn.setIcon(icon)
        self.open_btn.setObjectName("open_btn")
        self.open_layout.addWidget(self.open_btn)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.open_layout.addItem(spacerItem1)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.tools)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(80, 0, 52, 91))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.save_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.save_layout.setContentsMargins(0, 0, 0, 0)
        self.save_layout.setObjectName("save_layout")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.save_layout.addItem(spacerItem2)
        self.save_btn = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.save_btn.setMinimumSize(QtCore.QSize(50, 50))
        self.save_btn.setMaximumSize(QtCore.QSize(60, 60))
        self.save_btn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/resource/icons8-save-50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save_btn.setIcon(icon1)
        self.save_btn.setObjectName("save_btn")
        self.save_layout.addWidget(self.save_btn)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.save_layout.addItem(spacerItem3)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.tools)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(1040, 0, 52, 91))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.import_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.import_layout.setContentsMargins(0, 0, 0, 0)
        self.import_layout.setObjectName("import_layout")
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.import_layout.addItem(spacerItem4)
        self.import_btn = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.import_btn.setMinimumSize(QtCore.QSize(50, 50))
        self.import_btn.setMaximumSize(QtCore.QSize(60, 60))
        self.import_btn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/resource/icons8-import-50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.import_btn.setIcon(icon2)
        self.import_btn.setObjectName("import_btn")
        self.import_layout.addWidget(self.import_btn)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.import_layout.addItem(spacerItem5)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.tools)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(1110, 0, 52, 91))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.export_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.export_layout.setContentsMargins(0, 0, 0, 0)
        self.export_layout.setObjectName("export_layout")
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.export_layout.addItem(spacerItem6)
        self.export_btn = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.export_btn.setMinimumSize(QtCore.QSize(50, 50))
        self.export_btn.setMaximumSize(QtCore.QSize(60, 60))
        self.export_btn.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/resource/icons8-export-50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.export_btn.setIcon(icon3)
        self.export_btn.setObjectName("export_btn")
        self.export_layout.addWidget(self.export_btn)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.export_layout.addItem(spacerItem7)
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.tools)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(140, 0, 52, 91))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.rename_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.rename_layout.setContentsMargins(0, 0, 0, 0)
        self.rename_layout.setObjectName("rename_layout")
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.rename_layout.addItem(spacerItem8)
        self.rename_btn = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.rename_btn.setMinimumSize(QtCore.QSize(50, 50))
        self.rename_btn.setMaximumSize(QtCore.QSize(60, 60))
        self.rename_btn.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/resource/icons8-rename-50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rename_btn.setIcon(icon4)
        self.rename_btn.setObjectName("rename_btn")
        self.rename_layout.addWidget(self.rename_btn)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.rename_layout.addItem(spacerItem9)
        self.verticalLayout_2.addWidget(self.tools)
        self.content = QtWidgets.QFrame(self.centralwidget)
        self.content.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.content.setStyleSheet("background-color: rgb(204, 204, 204);")
        self.content.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.content.setObjectName("content")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.content)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.leftSide = QtWidgets.QFrame(self.content)
        self.leftSide.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.leftSide.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.leftSide.setFrameShadow(QtWidgets.QFrame.Raised)
        self.leftSide.setObjectName("leftSide")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.leftSide)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tableView = QtWidgets.QTableView(self.leftSide)
        self.tableView.setObjectName("tableView")
        self.verticalLayout_3.addWidget(self.tableView)
        self.horizontalLayout.addWidget(self.leftSide)
        self.verticalLayout_2.addWidget(self.content)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAction = QtWidgets.QMenu(self.menubar)
        self.menuAction.setObjectName("menuAction")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setIcon(icon)
        self.actionOpen.setIconVisibleInMenu(False)
        self.actionOpen.setObjectName("actionOpen")
        self.actionsave = QtWidgets.QAction(MainWindow)
        self.actionsave.setIcon(icon1)
        self.actionsave.setIconVisibleInMenu(False)
        self.actionsave.setObjectName("actionsave")
        self.actionSave_As = QtWidgets.QAction(MainWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionExport = QtWidgets.QAction(MainWindow)
        self.actionExport.setIcon(icon3)
        self.actionExport.setIconVisibleInMenu(False)
        self.actionExport.setObjectName("actionExport")
        self.actionImport = QtWidgets.QAction(MainWindow)
        self.actionImport.setIcon(icon2)
        self.actionImport.setIconVisibleInMenu(False)
        self.actionImport.setObjectName("actionImport")
        self.actionRename = QtWidgets.QAction(MainWindow)
        self.actionRename.setObjectName("actionRename")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionsave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuAction.addAction(self.actionExport)
        self.menuAction.addAction(self.actionImport)
        self.menuAction.addAction(self.actionRename)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAction.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuAction.setTitle(_translate("MainWindow", "Actions"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionsave.setText(_translate("MainWindow", "Save"))
        self.actionSave_As.setText(_translate("MainWindow", "Save As"))
        self.actionExport.setText(_translate("MainWindow", "Export"))
        self.actionImport.setText(_translate("MainWindow", "Import"))
        self.actionRename.setText(_translate("MainWindow", "Rename"))
import assets_rc