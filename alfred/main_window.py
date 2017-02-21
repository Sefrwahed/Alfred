# Qt imports
import os
from PyQt5.QtCore import Qt, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QVBoxLayout

from .ui.window_ui import Ui_MainWindow
from .module_groupbox import ModuleGroupBox
from .alfred_globals import modules_list_url

import requests
import json


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        # self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)

        self.url = modules_list_url
        self.modules_info = list({})

        self.pushButtonRetry.clicked.connect(self.setupMainWindow)

    def get_json(self):
        try:
            response = requests.get(self.url)
            return response.text
        except requests.exceptions.ConnectionError:
            return 0

    # def get_json(self):
    #     try:
    #         response = requests.get(self.url)
    #     except requests.exceptions.ConnectionError:
    #         pass
    #
    #     response = [{"id": 4,"name": "alfred-weather",
    #                  "description": "Fetch and see weather forecast on Alfred assistant",
    #                  "license": "mit","latest_version":{"number":"0.0.1","id":1}}, {
    #         "id": 6,"name": "alfred-app-exec","description": "Execute programs",
    #         "license": "mit","latest_version":{"number":"1.0.0","id":1}}]
    #     return response

    def parse_json(self):
        modules_list = json.loads(self.response)
        self.modules_info = modules_list

    def list_modules(self):
        self.verticalLayout_inner = QVBoxLayout()

        for module in self.modules_info:
            item = ModuleGroupBox(module)
            self.verticalLayout_inner.addWidget(item)
            self.modulesManager_tab.setLayout(self.verticalLayout_inner)

        self.groupBoxError.hide()

    def handleConnectionError(self):
        self.groupBoxError.show()
        self.labelError.setText("No Internet Connection")

    def setupMainWindow(self):
        self.response = self.get_json()
        if (self.response != 0):
            self.parse_json()
            self.list_modules()
        else:
            self.handleConnectionError()

    #overrides the show function :D
    def showEvent(self, QShowEvent):
        self.setupMainWindow()







