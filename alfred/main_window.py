# Qt imports
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QVBoxLayout

from .ui.window_ui import Ui_MainWindow
from .module_groupbox import ModuleGroupBox
from .alfred_globals import modules_list_url

import alfred.modules.download as download
import json


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.setAttribute(Qt.WA_TranslucentBackground, True)

        self.response = None
        self.verticalLayout_inner = None
        self.url = modules_list_url
        self.modules_info = list({})

        self.pushButtonRetry.clicked.connect(self.setup_main_window)

    def parse_json(self):
        modules_list = json.loads(self.response)
        # self.get_json()
        # modules_list = self.response
        self.modules_info = modules_list

    def list_modules(self):
        self.verticalLayout_inner = QVBoxLayout()

        for module in self.modules_info:
            item = ModuleGroupBox(module)
            self.verticalLayout_inner.addWidget(item, alignment=Qt.AlignTop)

        self.modulesManager_tab.setLayout(self.verticalLayout_inner)

        self.groupBoxError.hide()

    def handle_connection_error(self):
        self.groupBoxError.show()
        self.labelError.setText("No Internet Connection")

    def setup_main_window(self):
        self.response = download.download(self.url)
        if self.response != 0:
            self.parse_json()
            self.list_modules()
        else:
            self.handle_connection_error()

    def showEvent(self, QShowEvent):
        self.setup_main_window()
