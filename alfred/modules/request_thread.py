import requests
import urllib.request
import json

# Qt imports
from PyQt5.QtCore import QThread, pyqtSignal

# Local imports
from alfred import alfred_globals as ag
from alfred.logger import Logger


class RequestThread(QThread):
    signal_finished = pyqtSignal()

    def __init__(self):
        QThread.__init__(self)
        self.purpose = None
        self.conn_err = False
        self.data = None

    def __del__(self):
        self.wait()

    def run(self):
        self.conn_err = False
        if self.purpose == "list":
            self.list_modules()
        elif self.purpose == "download":
            self.download()

        Logger().info("Request Thread finished")
        self.signal_finished.emit()

    def download(self):
        try:
            Logger().info("Downloading zip file...")
            urllib.request.urlretrieve(self.url, self.zip_path)
            Logger().info("Downloaded successfully")
        except:
            Logger().err("Connection failed while downloading zip file")
            self.conn_err = True

    def list_modules(self):
        try:
            Logger().info("Fetching modules list from AlfredHub...")
            resp = requests.get(ag.modules_list_url)
            self.data = json.loads(resp.text)
            Logger().info("Fetched modules list from AlfredHub successfully")
        except:
            Logger().err("Connection failed while fetching modules list")
            self.conn_err = True
