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
        GroupBox.resize(634, 104)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(GroupBox.sizePolicy().hasHeightForWidth())
        GroupBox.setSizePolicy(sizePolicy)
        GroupBox.setStyleSheet("QGroupBox{\n"
"    border:none\n"
"\n"
"}")
        GroupBox.setTitle("")
        self.pushButton = QtWidgets.QPushButton(GroupBox)
        self.pushButton.setGeometry(QtCore.QRect(540, 40, 91, 27))
        self.pushButton.setObjectName("pushButton")
        self.verticalLayoutWidget = QtWidgets.QWidget(GroupBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 521, 89))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelName = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelName.sizePolicy().hasHeightForWidth())
        self.labelName.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MathJax_Caligraphic")
        font.setPointSize(16)
        self.labelName.setFont(font)
        self.labelName.setStyleSheet("QLabel{\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"    color: rgb(243, 243, 243);\n"
"}")
        self.labelName.setObjectName("labelName")
        self.verticalLayout.addWidget(self.labelName)
        self.labelDesc = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelDesc.sizePolicy().hasHeightForWidth())
        self.labelDesc.setSizePolicy(sizePolicy)
        self.labelDesc.setStyleSheet("QLabel{\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"    color: rgb(243, 243, 243);\n"
"}")
        self.labelDesc.setObjectName("labelDesc")
        self.verticalLayout.addWidget(self.labelDesc)
        self.labelVersion = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelVersion.sizePolicy().hasHeightForWidth())
        self.labelVersion.setSizePolicy(sizePolicy)
        self.labelVersion.setStyleSheet("QLabel{\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"    color: rgb(243, 243, 243);\n"
"}")
        self.labelVersion.setObjectName("labelVersion")
        self.verticalLayout.addWidget(self.labelVersion)
        self.labelLicense = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelLicense.sizePolicy().hasHeightForWidth())
        self.labelLicense.setSizePolicy(sizePolicy)
        self.labelLicense.setStyleSheet("QLabel{\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"    color: rgb(243, 243, 243);\n"
"}")
        self.labelLicense.setObjectName("labelLicense")
        self.verticalLayout.addWidget(self.labelLicense)
        self.pushButton.raise_()
        self.verticalLayoutWidget.raise_()
        self.labelLicense.raise_()

        self.retranslateUi(GroupBox)
        QtCore.QMetaObject.connectSlotsByName(GroupBox)

    def retranslateUi(self, GroupBox):
        _translate = QtCore.QCoreApplication.translate
        GroupBox.setWindowTitle(_translate("GroupBox", "GroupBox"))
        self.pushButton.setText(_translate("GroupBox", "Install"))
        self.labelName.setText(_translate("GroupBox", "TextLabel"))
        self.labelDesc.setText(_translate("GroupBox", "TextLabel"))
        self.labelVersion.setText(_translate("GroupBox", "TextLabel"))
        self.labelLicense.setText(_translate("GroupBox", "TextLabel"))

