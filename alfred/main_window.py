# Qt imports
from PyQt5.QtCore import Qt
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

    def showEvent(self, QShowEvent):
        self.setupMainWindow()
