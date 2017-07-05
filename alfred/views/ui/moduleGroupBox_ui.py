# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'moduleGroupBox.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_GroupBox(object):
    def setupUi(self, GroupBox):
        GroupBox.setObjectName("GroupBox")
        GroupBox.resize(635, 131)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(GroupBox.sizePolicy().hasHeightForWidth())
        GroupBox.setSizePolicy(sizePolicy)
        GroupBox.setStyleSheet("QGroupBox{\n"
"    border:none\n"
"\n"
"}")
        GroupBox.setTitle("")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(GroupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.labelName_2 = QtWidgets.QLabel(GroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelName_2.sizePolicy().hasHeightForWidth())
        self.labelName_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MathJax_Caligraphic")
        font.setPointSize(16)
        self.labelName_2.setFont(font)
        self.labelName_2.setStyleSheet("QLabel{\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"    color: rgb(243, 243, 243);\n"
"}")
        self.labelName_2.setObjectName("labelName_2")
        self.verticalLayout_2.addWidget(self.labelName_2)
        self.labelDesc_2 = QtWidgets.QLabel(GroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelDesc_2.sizePolicy().hasHeightForWidth())
        self.labelDesc_2.setSizePolicy(sizePolicy)
        self.labelDesc_2.setStyleSheet("QLabel{\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"    color: rgb(243, 243, 243);\n"
"}")
        self.labelDesc_2.setObjectName("labelDesc_2")
        self.verticalLayout_2.addWidget(self.labelDesc_2)
        self.labelVersion_2 = QtWidgets.QLabel(GroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelVersion_2.sizePolicy().hasHeightForWidth())
        self.labelVersion_2.setSizePolicy(sizePolicy)
        self.labelVersion_2.setStyleSheet("QLabel{\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"    color: rgb(243, 243, 243);\n"
"}")
        self.labelVersion_2.setObjectName("labelVersion_2")
        self.verticalLayout_2.addWidget(self.labelVersion_2)
        self.labelLicense_2 = QtWidgets.QLabel(GroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelLicense_2.sizePolicy().hasHeightForWidth())
        self.labelLicense_2.setSizePolicy(sizePolicy)
        self.labelLicense_2.setStyleSheet("QLabel{\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"    color: rgb(243, 243, 243);\n"
"}")
        self.labelLicense_2.setObjectName("labelLicense_2")
        self.verticalLayout_2.addWidget(self.labelLicense_2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.pushButton = QtWidgets.QPushButton(GroupBox)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.pushButton.raise_()

        self.retranslateUi(GroupBox)
        QtCore.QMetaObject.connectSlotsByName(GroupBox)

    def retranslateUi(self, GroupBox):
        _translate = QtCore.QCoreApplication.translate
        GroupBox.setWindowTitle(_translate("GroupBox", "GroupBox"))
        self.labelName_2.setText(_translate("GroupBox", "TextLabel"))
        self.labelDesc_2.setText(_translate("GroupBox", "TextLabel"))
        self.labelVersion_2.setText(_translate("GroupBox", "TextLabel"))
        self.labelLicense_2.setText(_translate("GroupBox", "TextLabel"))
        self.pushButton.setText(_translate("GroupBox", "Install"))

