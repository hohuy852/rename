# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './TypeSelect.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Type_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(263, 109)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.open_folder = QtWidgets.QPushButton(self.frame)
        self.open_folder.setObjectName("open_folder")
        self.horizontalLayout_2.addWidget(self.open_folder)
        self.open_file = QtWidgets.QPushButton(self.frame)
        self.open_file.setObjectName("open_file")
        self.horizontalLayout_2.addWidget(self.open_file)
        self.horizontalLayout.addWidget(self.frame)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.open_folder.setText(_translate("Dialog", "Load Folder"))
        self.open_file.setText(_translate("Dialog", "Load Files"))
