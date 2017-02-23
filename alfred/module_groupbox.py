import os
import string
import urllib.request

# Qt imports
from PyQt5.QtWidgets import QGroupBox

from .ui.moduleGroupBox_ui import Ui_GroupBox
from .alfred_globals import user_folder_path
from .alfred_globals import modules_download_url
from .modules.install import install


class ModuleGroupBox(QGroupBox, Ui_GroupBox):

    def __init__(self, module_info):
        QGroupBox.__init__(self)
        self.setupUi(self)

        self.module = module_info
        self.setData()

        self.download_url = modules_download_url
        self.pushButton.clicked.connect(self.download_zip)

    # @pyqtSlot()
    def setData(self):

        name = self.module["name"]
        name = name.replace('-',' ')
        name = string.capwords(name)
        self.labelName_2.setText(name)
        self.labelDesc_2.setText(self.module["description"])
        self.labelLicense_2.setText(self.module["license"])
        latestVersion= self.module["latest_version"]
        self.labelVersion_2.setText(latestVersion["number"])

    def enableButton(self, enable):
        self.pushButton.enabled = enable

    def download_zip(self):
        self.pushButton.setText("installing..")
        self.pushButton.enabled = False

        module = self.module
        url = (self.download_url.replace("<id>", str(module["id"]))) \
         .replace("<latest_vesrsion_id>", str(module["latest_version"]["id"]))
        zip_path = os.path.join(user_folder_path, module["name"])
        urllib.request.urlretrieve(url, zip_path)

        install(module, zip_path)

        self.pushButton.setText("installed")
