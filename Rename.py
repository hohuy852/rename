# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './Rename.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Rename_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(399, 328)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.frame)
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.groupBox.setStyleSheet("border-color: rgb(0, 0, 0);")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.custom = QtWidgets.QRadioButton(self.groupBox)
        self.custom.setCheckable(True)
        self.custom.setObjectName("custom")
        self.verticalLayout_2.addWidget(self.custom)
        self.manual = QtWidgets.QRadioButton(self.groupBox)
        self.manual.setObjectName("manual")
        self.verticalLayout_2.addWidget(self.manual)
        self.frame_2 = QtWidgets.QFrame(self.groupBox)
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 41))
        self.frame_2.setStyleSheet("padding-left: 10px;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.newName = QtWidgets.QLineEdit(self.frame_2)
        self.newName.setStyleSheet("QLineEdit{\n"
"    border: 1px solid #000;\n"
"    border-radius: 3px;\n"
"    font-size: 14px;\n"
"    padding: 0 3px;\n"
"}")
        self.newName.setObjectName("newName")
        self.horizontalLayout_2.addWidget(self.newName)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.frame_5 = QtWidgets.QFrame(self.groupBox)
        self.frame_5.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_6 = QtWidgets.QFrame(self.frame_5)
        self.frame_6.setMaximumSize(QtCore.QSize(52, 16777215))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.label_2 = QtWidgets.QLabel(self.frame_6)
        self.label_2.setGeometry(QtCore.QRect(22, -2, 28, 16))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.frame_6)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.radioButton = QtWidgets.QRadioButton(self.frame_5)
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout_3.addWidget(self.radioButton)
        self.radioButton_4 = QtWidgets.QRadioButton(self.frame_5)
        self.radioButton_4.setObjectName("radioButton_4")
        self.verticalLayout_3.addWidget(self.radioButton_4)
        self.radioButton_3 = QtWidgets.QRadioButton(self.frame_5)
        self.radioButton_3.setObjectName("radioButton_3")
        self.verticalLayout_3.addWidget(self.radioButton_3)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.verticalLayout_2.addWidget(self.frame_5)
        self.frame_3 = QtWidgets.QFrame(self.groupBox)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_2.addWidget(self.frame_3)
        self.verticalLayout.addWidget(self.groupBox)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 32))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.cancel_btn = QtWidgets.QPushButton(self.frame_4)
        self.cancel_btn.setGeometry(QtCore.QRect(283, 10, 75, 23))
        self.cancel_btn.setObjectName("cancel_btn")
        self.confirm_btn = QtWidgets.QPushButton(self.frame_4)
        self.confirm_btn.setGeometry(QtCore.QRect(200, 10, 75, 23))
        self.confirm_btn.setObjectName("confirm_btn")
        self.verticalLayout.addWidget(self.frame_4)
        self.horizontalLayout.addWidget(self.frame)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox.setTitle(_translate("Dialog", "Settings"))
        self.custom.setText(_translate("Dialog", "Custom from template"))
        self.manual.setText(_translate("Dialog", "Auto"))
        self.label.setText(_translate("Dialog", "Name"))
        self.label_2.setText(_translate("Dialog", "Prefix"))
        self.radioButton.setText(_translate("Dialog", "Date"))
        self.radioButton_4.setText(_translate("Dialog", "Index"))
        self.radioButton_3.setText(_translate("Dialog", "Name + index"))
        self.cancel_btn.setText(_translate("Dialog", "Cancel"))
        self.confirm_btn.setText(_translate("Dialog", "Confirm"))
