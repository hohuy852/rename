# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'change-dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QRadioButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(399, 328)
        self.horizontalLayout = QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(self.frame)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMaximumSize(QSize(16777215, 16777215))
        self.groupBox.setStyleSheet(u"border-color: rgb(0, 0, 0);")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.manual = QRadioButton(self.groupBox)
        self.manual.setObjectName(u"manual")

        self.verticalLayout_2.addWidget(self.manual)

        self.frame_2 = QFrame(self.groupBox)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 41))
        self.frame_2.setStyleSheet(u"padding-left: 10px;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.newName = QLineEdit(self.frame_2)
        self.newName.setObjectName(u"newName")
        self.newName.setStyleSheet(u"QLineEdit{\n"
"	border: 1px solid #000;\n"
"	border-radius: 3px;\n"
"	font-size: 14px;\n"
"	padding: 0 3px;\n"
"}")

        self.horizontalLayout_2.addWidget(self.newName)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.excel = QRadioButton(self.groupBox)
        self.excel.setObjectName(u"excel")

        self.verticalLayout_2.addWidget(self.excel)

        self.frame_3 = QFrame(self.groupBox)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.groupBox)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(16777215, 32))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.cancel_btn = QPushButton(self.frame_4)
        self.cancel_btn.setObjectName(u"cancel_btn")
        self.cancel_btn.setGeometry(QRect(283, 10, 75, 23))
        self.confirm_btn = QPushButton(self.frame_4)
        self.confirm_btn.setObjectName(u"confirm_btn")
        self.confirm_btn.setGeometry(QRect(200, 10, 75, 23))

        self.verticalLayout.addWidget(self.frame_4)


        self.horizontalLayout.addWidget(self.frame)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"Settings", None))
        self.manual.setText(QCoreApplication.translate("Dialog", u"Manual", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Name", None))
        self.excel.setText(QCoreApplication.translate("Dialog", u"Excel", None))
        self.cancel_btn.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.confirm_btn.setText(QCoreApplication.translate("Dialog", u"Confirm", None))
    # retranslateUi

