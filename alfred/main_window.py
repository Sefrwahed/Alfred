# Qt imports
from PyQt5.QtCore import Qt, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QMainWindow

from .ui.window_ui import Ui_MainWindow

import requests
import json
import urllib.request


class MainWindow(QMainWindow, Ui_MainWindow):
    text_changed = pyqtSignal('QString')

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)

        self.url = 'https://alfredhub.herokuapp.com/alfred_modules.json'
        self.download_url = \
            'http://alfredhub.herokuapp.com/alfred_modules/<id>/versions/<latest_vesrsion_id>/download'
        self.modules_info = list({})
        self.parse_json()
        self.download_zip(self.modules_info)


    @pyqtSlot()
    def setModules(self):
        pass

    def get_json(self):
        response = requests.get(self.url)
        return response.text

    def parse_json(self):
        response = self.get_json()
        modules_list = json.loads(response)
        self.modules_info = modules_list

    def download_zip(self, modules_info):
        for module in modules_info:
            url = (self.download_url.replace("<id>", str(module["id"]))) \
                .replace("<latest_vesrsion_id>", str(1))
            zip_path = '/home/shimaa/.alfred/modules/' + module["name"]
            urllib.request.urlretrieve(url, zip_path)


