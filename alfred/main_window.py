# Qt imports
import os
from PyQt5.QtCore import Qt, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QMainWindow

from .ui.window_ui import Ui_MainWindow
from .module_groupbox import ModuleGroupBox
from .alfred_globals import modules_list_url

import requests
import json


class MainWindow(QMainWindow, Ui_MainWindow):
    text_changed = pyqtSignal('QString')

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

        # self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)

        self.url = modules_list_url
        self.modules_info = list({})
        self.parse_json()
        self.list_modules()


    def get_json(self):
        response = requests.get(self.url)
        return response.text

    def parse_json(self):
        response = self.get_json()
        modules_list = json.loads(response)
        self.modules_info = modules_list

    def list_modules(self):
        for module in self.modules_info:
            item = ModuleGroupBox(module)
            self.verticalLayout_inner.addWidget(item)






