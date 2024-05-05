# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './App-ver2.ui'
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
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.main = QtWidgets.QFrame(self.centralwidget)
        self.main.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main.setObjectName("main")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.main)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.leftnav = QtWidgets.QFrame(self.main)
        self.leftnav.setMinimumSize(QtCore.QSize(191, 0))
        self.leftnav.setMaximumSize(QtCore.QSize(209, 16777215))
        font = QtGui.QFont()
        font.setFamily("Poppins SemiBold")
        font.setBold(True)
        self.leftnav.setFont(font)
        self.leftnav.setStyleSheet("")
        self.leftnav.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.leftnav.setFrameShadow(QtWidgets.QFrame.Raised)
        self.leftnav.setObjectName("leftnav")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.leftnav)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.top_btns = QtWidgets.QFrame(self.leftnav)
        self.top_btns.setMinimumSize(QtCore.QSize(0, 0))
        self.top_btns.setStyleSheet("QPushButton{\n"
"text-align:left;\n"
"}")
        self.top_btns.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.top_btns.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top_btns.setObjectName("top_btns")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.top_btns)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.info = QtWidgets.QFrame(self.top_btns)
        self.info.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.info.setFrameShadow(QtWidgets.QFrame.Raised)
        self.info.setObjectName("info")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.info)
        self.horizontalLayout_4.setContentsMargins(0, -1, 0, 68)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.usericon = QtWidgets.QLabel(self.info)
        self.usericon.setMaximumSize(QtCore.QSize(44, 16777215))
        self.usericon.setText("")
        self.usericon.setPixmap(QtGui.QPixmap(":/icons/profile.png"))
        self.usericon.setObjectName("usericon")
        self.horizontalLayout_4.addWidget(self.usericon)
        self.frame = QtWidgets.QFrame(self.info)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 58))
        font = QtGui.QFont()
        font.setFamily("Poppins ExtraBold")
        font.setPointSize(12)
        font.setBold(True)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 13))
        font = QtGui.QFont()
        font.setFamily("Poppins SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(202, 202, 202);")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_7.addWidget(self.label_2, 0, QtCore.Qt.AlignBottom)
        self.name = QtWidgets.QLabel(self.frame)
        self.name.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Poppins SemiBold")
        font.setPointSize(10)
        font.setItalic(False)
        self.name.setFont(font)
        self.name.setStyleSheet("font: 600 10pt \"Poppins SemiBold\";")
        self.name.setWordWrap(False)
        self.name.setObjectName("name")
        self.verticalLayout_7.addWidget(self.name, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout_4.addWidget(self.frame)
        self.verticalLayout_3.addWidget(self.info)
        self.renamer_btn = QtWidgets.QPushButton(self.top_btns)
        self.renamer_btn.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Poppins SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        self.renamer_btn.setFont(font)
        self.renamer_btn.setStyleSheet("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/rename.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.renamer_btn.setIcon(icon)
        self.renamer_btn.setIconSize(QtCore.QSize(25, 25))
        self.renamer_btn.setFlat(True)
        self.renamer_btn.setObjectName("renamer_btn")
        self.verticalLayout_3.addWidget(self.renamer_btn)
        self.pdfcounter_btn = QtWidgets.QPushButton(self.top_btns)
        self.pdfcounter_btn.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Poppins SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        self.pdfcounter_btn.setFont(font)
        self.pdfcounter_btn.setStyleSheet("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/folder-menu.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pdfcounter_btn.setIcon(icon1)
        self.pdfcounter_btn.setIconSize(QtCore.QSize(25, 25))
        self.pdfcounter_btn.setFlat(True)
        self.pdfcounter_btn.setObjectName("pdfcounter_btn")
        self.verticalLayout_3.addWidget(self.pdfcounter_btn)
        self.verticalLayout_2.addWidget(self.top_btns, 0, QtCore.Qt.AlignTop)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.bot_btns = QtWidgets.QFrame(self.leftnav)
        self.bot_btns.setMinimumSize(QtCore.QSize(0, 100))
        self.bot_btns.setStyleSheet("QPushButton{\n"
"text-align:left;\n"
"}")
        self.bot_btns.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bot_btns.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bot_btns.setObjectName("bot_btns")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.bot_btns)
        self.verticalLayout_6.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.about_btn = QtWidgets.QPushButton(self.bot_btns)
        font = QtGui.QFont()
        font.setFamily("Poppins SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        self.about_btn.setFont(font)
        self.about_btn.setStyleSheet("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/profile.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.about_btn.setIcon(icon2)
        self.about_btn.setIconSize(QtCore.QSize(25, 25))
        self.about_btn.setFlat(True)
        self.about_btn.setObjectName("about_btn")
        self.verticalLayout_6.addWidget(self.about_btn)
        self.logout_btn = QtWidgets.QPushButton(self.bot_btns)
        font = QtGui.QFont()
        font.setFamily("Poppins SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        self.logout_btn.setFont(font)
        self.logout_btn.setStyleSheet("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/support.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.logout_btn.setIcon(icon3)
        self.logout_btn.setIconSize(QtCore.QSize(25, 25))
        self.logout_btn.setFlat(True)
        self.logout_btn.setObjectName("logout_btn")
        self.verticalLayout_6.addWidget(self.logout_btn)
        self.pushButton_4 = QtWidgets.QPushButton(self.bot_btns)
        font = QtGui.QFont()
        font.setFamily("Poppins SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/logout.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon4)
        self.pushButton_4.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_4.setFlat(True)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_6.addWidget(self.pushButton_4)
        self.verticalLayout_2.addWidget(self.bot_btns)
        self.horizontalLayout.addWidget(self.leftnav)
        self.main_2 = QtWidgets.QStackedWidget(self.main)
        self.main_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.main_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 18px;")
        self.main_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.main_2.setObjectName("main_2")
        self.main_2Page1_2 = QtWidgets.QWidget()
        self.main_2Page1_2.setObjectName("main_2Page1_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.main_2Page1_2)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_2 = QtWidgets.QFrame(self.main_2Page1_2)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 129))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 129))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Poppins SemiBold")
        font.setPointSize(11)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label)
        self.tools = QtWidgets.QFrame(self.frame_2)
        self.tools.setMinimumSize(QtCore.QSize(0, 78))
        self.tools.setMaximumSize(QtCore.QSize(16777215, 100))
        self.tools.setStyleSheet("QFrame{border: 1px solid #AEAEAE;\n"
"background-color: rgb(246, 246, 248);\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton{\n"
"border: 1px solid #AEAEAE;\n"
"border-radius: 10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));\n"
"}\n"
"QPushButton::hover{\n"
"background-color: #fff;\n"
"}\n"
"")
        self.tools.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tools.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tools.setObjectName("tools")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tools)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.open_btn = QtWidgets.QPushButton(self.tools)
        self.open_btn.setMinimumSize(QtCore.QSize(48, 48))
        self.open_btn.setMaximumSize(QtCore.QSize(48, 48))
        self.open_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.open_btn.setToolTipDuration(-5)
        self.open_btn.setStyleSheet("")
        self.open_btn.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/folder-open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.open_btn.setIcon(icon5)
        self.open_btn.setIconSize(QtCore.QSize(28, 28))
        self.open_btn.setFlat(True)
        self.open_btn.setObjectName("open_btn")
        self.horizontalLayout_2.addWidget(self.open_btn)
        self.rename_btn = QtWidgets.QPushButton(self.tools)
        self.rename_btn.setMinimumSize(QtCore.QSize(48, 48))
        self.rename_btn.setMaximumSize(QtCore.QSize(48, 48))
        self.rename_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.rename_btn.setStyleSheet("")
        self.rename_btn.setText("")
        self.rename_btn.setIcon(icon)
        self.rename_btn.setIconSize(QtCore.QSize(28, 28))
        self.rename_btn.setFlat(True)
        self.rename_btn.setObjectName("rename_btn")
        self.horizontalLayout_2.addWidget(self.rename_btn)
        self.export_btn = QtWidgets.QPushButton(self.tools)
        self.export_btn.setMinimumSize(QtCore.QSize(48, 48))
        self.export_btn.setMaximumSize(QtCore.QSize(48, 48))
        self.export_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.export_btn.setStyleSheet("")
        self.export_btn.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/export.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.export_btn.setIcon(icon6)
        self.export_btn.setIconSize(QtCore.QSize(28, 28))
        self.export_btn.setFlat(True)
        self.export_btn.setObjectName("export_btn")
        self.horizontalLayout_2.addWidget(self.export_btn)
        self.import_btn = QtWidgets.QPushButton(self.tools)
        self.import_btn.setMinimumSize(QtCore.QSize(48, 48))
        self.import_btn.setMaximumSize(QtCore.QSize(48, 48))
        self.import_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.import_btn.setStyleSheet("")
        self.import_btn.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/import.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.import_btn.setIcon(icon7)
        self.import_btn.setIconSize(QtCore.QSize(28, 28))
        self.import_btn.setFlat(True)
        self.import_btn.setObjectName("import_btn")
        self.horizontalLayout_2.addWidget(self.import_btn)
        self.test_btn = QtWidgets.QPushButton(self.tools)
        self.test_btn.setMinimumSize(QtCore.QSize(48, 48))
        self.test_btn.setMaximumSize(QtCore.QSize(48, 48))
        self.test_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.test_btn.setStyleSheet("")
        self.test_btn.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(".\\resource/test.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.test_btn.setIcon(icon8)
        self.test_btn.setIconSize(QtCore.QSize(28, 28))
        self.test_btn.setFlat(True)
        self.test_btn.setObjectName("test_btn")
        self.horizontalLayout_2.addWidget(self.test_btn)
        self.filter_btn = QtWidgets.QPushButton(self.tools)
        self.filter_btn.setMinimumSize(QtCore.QSize(48, 48))
        self.filter_btn.setMaximumSize(QtCore.QSize(48, 48))
        self.filter_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.filter_btn.setStyleSheet("")
        self.filter_btn.setText("")
        self.filter_btn.setIcon(icon8)
        self.filter_btn.setIconSize(QtCore.QSize(28, 28))
        self.filter_btn.setFlat(True)
        self.filter_btn.setObjectName("filter_btn")
        self.horizontalLayout_2.addWidget(self.filter_btn)
        spacerItem1 = QtWidgets.QSpacerItem(704, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_5.addWidget(self.tools)
        spacerItem2 = QtWidgets.QSpacerItem(20, 541, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem2)
        self.verticalLayout_4.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.main_2Page1_2)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 565))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.tableView = QtWidgets.QTableView(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Poppins SemiBold")
        font.setPointSize(8)
        font.setBold(True)
        self.tableView.setFont(font)
        self.tableView.setStyleSheet("QHeaderView::section{\n"
"background-color:rgb(174, 174, 174);\n"
"color: white;\n"
"border: 1px solid #fff;\n"
"text-align:center;\n"
"font-family: \'Poppins SemiBold\', sans-serif;\n"
"}\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: rgb(255, 255, 255);\n"
"    width: 7px;\n"
"    margin: 6px 0 6px 0;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"/*  HANDLE BAR VERTICAL */\n"
"QScrollBar::handle:vertical {\n"
"    background-color: rgb(174, 174, 174);\n"
"    min-height: 30px;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    background-color: rgb(174, 174, 174);\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:pressed {\n"
"    background-color: rgb(174, 174, 174);\n"
"}\n"
"\n"
"/* BTN TOP - SCROLLBAR */\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background-color: rgb(105, 105, 105);\n"
"    height: 7px;\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover {\n"
"    background-color: rgb(105, 105, 105);\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:pressed {\n"
"    background-color: rgb(105, 105, 105);\n"
"}\n"
"\n"
"/* BTN BOTTOM - SCROLLBAR */\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background-color: rgb(105, 105, 105);\n"
"    height: 7px;\n"
"    border-bottom-left-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:hover {\n"
"    background-color: rgb(105, 105, 105);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:pressed {\n"
"    background-color: rgb(105, 105, 105);\n"
"}\n"
"\n"
"/* RESET ARROW */\n"
"QScrollBar::up-arrow:vertical,\n"
"QScrollBar::down-arrow:vertical {\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical,\n"
"QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}\n"
"\n"
"/* HORIZONTAL SCROLLBAR - HOMEWORK */\n"
"QScrollBar:horizontal {}\n"
"\n"
"QScrollBar::handle:horizontal {}\n"
"\n"
"QScrollBar::add-line:horizontal {}\n"
"\n"
"QScrollBar::sub-line:horizontal {}\n"
"\n"
"QScrollBar::up-arrow:horizontal,\n"
"QScrollBar::down-arrow:horizontal {}\n"
"\n"
"QScrollBar::add-page:horizontal,\n"
"QScrollBar::sub-page:horizontal {}\n"
"\n"
"")
        self.tableView.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableView.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableView.setObjectName("tableView")
        self.verticalLayout_8.addWidget(self.tableView)
        self.verticalLayout_4.addWidget(self.frame_3)
        self.main_2.addWidget(self.main_2Page1_2)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.label_4 = QtWidgets.QLabel(self.page)
        self.label_4.setGeometry(QtCore.QRect(440, 350, 49, 16))
        self.label_4.setObjectName("label_4")
        self.main_2.addWidget(self.page)
        self.horizontalLayout.addWidget(self.main_2)
        self.verticalLayout.addWidget(self.main)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.main_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Welcome back,"))
        self.name.setText(_translate("MainWindow", "syhuy851"))
        self.renamer_btn.setText(_translate("MainWindow", "  Renamer"))
        self.pdfcounter_btn.setText(_translate("MainWindow", "  Pdf Counter"))
        self.about_btn.setText(_translate("MainWindow", "  About"))
        self.logout_btn.setText(_translate("MainWindow", "  Support"))
        self.pushButton_4.setText(_translate("MainWindow", "  Logout"))
        self.label.setText(_translate("MainWindow", "Functions"))
        self.open_btn.setToolTip(_translate("MainWindow", "Open"))
        self.label_4.setText(_translate("MainWindow", "Page 2"))
import icons_rc
