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
        MainWindow.resize(790, 430)
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
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.modulesManager_tab)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(-1, 0, 771, 381))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_inner = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_inner.setObjectName("verticalLayout_inner")
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
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.modulesManager_tab), _translate("MainWindow", "Modules Manager"))

