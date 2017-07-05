# Python builtins
import os

# PyQt imports
from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings
from PyQt5.QtCore import QUrl, QMetaObject, QRect, QFileInfo


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(808, 595)

        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setStyleSheet(
            "QFrame{ background-color: rgba(33,34,34,.96); }\n"
        )
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setContentsMargins(80, 40, 80, 40)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.bot_status_icon = QWebEngineView(self.frame)
        self.bot_status_icon.setStyleSheet(
            "QWebEngineView { \n"
            "    background-color: rgba(0, 0, 0, 0);\n"
            "}"
        )
        self.bot_status_icon.page().setBackgroundColor(QtCore.Qt.transparent)
        self.bot_status_icon.setMaximumSize(QtCore.QSize(70, 70))
        curr_dir = os.path.dirname(__file__)
        bot_icon_html_url = QUrl.fromLocalFile(
            QFileInfo(curr_dir + '/bot_status_icon.html').absoluteFilePath()
        )
        self.bot_status_icon.page().load(bot_icon_html_url)

        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setStyleSheet(
            "QLineEdit { \n"
            "    background-color: rgba(0, 0, 0, 0);\n"
            "    color: rgb(243, 243, 243);\n"
            "    font-size: 40px;\n"
            "    padding: 8px;\n"
            "    border: 5px solid rgb(6, 184, 251);\n"
            "    border-style: none none solid none;\n"
            "}"
        )
        self.lineEdit.setFrame(True)
        self.lineEdit.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.lineEdit.setObjectName("lineEdit")

        self.horizontalLayout.addWidget(self.bot_status_icon)
        self.horizontalLayout.addWidget(self.lineEdit)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.scrollArea = QtWidgets.QScrollArea(self.frame)
        self.scrollArea.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")

        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 642, 404))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.webView = QtWebEngineWidgets.QWebEngineView(
            self.scrollAreaWidgetContents
        )

        self.webView.page().settings().setAttribute(QWebEngineSettings.LocalContentCanAccessFileUrls, True)
        self.webView.setStyleSheet(
            "QWebEngineView { \n"
            "    background-color: rgba(0, 0, 0, 0);\n"
            "}"
        )
        self.webView.setObjectName("webView")
        self.webView.show()
        self.webView.page().setBackgroundColor(QtCore.Qt.transparent)

        self.gridLayout.addWidget(self.webView, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(Dialog)
        QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.lineEdit.setPlaceholderText(
            _translate("Dialog", "ask me anything...")
        )
