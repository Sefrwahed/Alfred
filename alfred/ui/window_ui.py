# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(806, 564)
        MainWindow.setStyleSheet("QFrame{ background-color: rgba(33,34,34,.96); }")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QFrame{ background-color: rgba(33,34,34,.96); }")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 771, 531))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.verticalLayoutWidget)
        self.tabWidget.setAutoFillBackground(True)
        self.tabWidget.setStyleSheet("QFrame{ background-color: rgba(33,34,34,.96); }")
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideRight)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.modulesManager_tab = QtWidgets.QWidget()
        self.modulesManager_tab.setObjectName("modulesManager_tab")
        self.groupBoxError = QtWidgets.QGroupBox(self.modulesManager_tab)
        self.groupBoxError.setGeometry(QtCore.QRect(230, 220, 291, 51))
        self.groupBoxError.setStyleSheet("QGroupBox{\n"
"    border:none\n"
"}")
        self.groupBoxError.setTitle("")
        self.groupBoxError.setObjectName("groupBoxError")
        self.labelError = QtWidgets.QLabel(self.groupBoxError)
        self.labelError.setEnabled(True)
        self.labelError.setGeometry(QtCore.QRect(40, 10, 151, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelError.sizePolicy().hasHeightForWidth())
        self.labelError.setSizePolicy(sizePolicy)
        self.labelError.setStyleSheet("QLabel{\n"
"    color:rgb(243,243,243)\n"
"\n"
"}")
        self.labelError.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.labelError.setFrameShadow(QtWidgets.QFrame.Plain)
        self.labelError.setScaledContents(False)
        self.labelError.setAlignment(QtCore.Qt.AlignCenter)
        self.labelError.setObjectName("labelError")
        self.pushButtonRetry = QtWidgets.QPushButton(self.groupBoxError)
        self.pushButtonRetry.setGeometry(QtCore.QRect(210, 11, 41, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonRetry.sizePolicy().hasHeightForWidth())
        self.pushButtonRetry.setSizePolicy(sizePolicy)
        self.pushButtonRetry.setMaximumSize(QtCore.QSize(41, 16777215))
        self.pushButtonRetry.setStyleSheet("")
        self.pushButtonRetry.setObjectName("pushButtonRetry")
        self.tabWidget.addTab(self.modulesManager_tab, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelError.setText(_translate("MainWindow", "Error"))
        self.pushButtonRetry.setText(_translate("MainWindow", "Retry"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.modulesManager_tab), _translate("MainWindow", "Modules Manager"))
