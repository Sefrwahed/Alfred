import os
import string
import urllib.request
from enum import Enum


# Qt imports
from PyQt5.QtWidgets import QGroupBox

from .ui.moduleGroupBox_ui import Ui_GroupBox
from .alfred_globals import user_folder_path
from .alfred_globals import modules_download_url
from .modules.install import install
from .modules.install import uninstall
from .modules.install import update
from .modules.module_info import get_module_by_id
import alfred.logger as logger


class ButtonState(Enum):
    UNINSTALL = "Uninstall"
    INSTALL = "Install"
    UPDATE = "Update"


class ModuleGroupBox(QGroupBox, Ui_GroupBox):

    def __init__(self, module_info):
        QGroupBox.__init__(self)
        self.setupUi(self)
        self.buttonState = None
        self.name = None

        self.module = module_info
        self.set_data()

        self.download_url = modules_download_url
        self.pushButton.clicked.connect(self.click_action)

    def set_data(self):

        self.name = self.module["name"]
        self.name = self.name.replace('-', ' ')
        self.name = string.capwords(self.name)

        latest_version = self.module["latest_version"]["number"]

        self.labelName_2.setText(self.name)
        self.labelDesc_2.setText(self.module["description"])
        self.labelLicense_2.setText(self.module["license"])
        self.labelVersion_2.setText(latest_version)

        installed_module = get_module_by_id(self.module["id"])
        if installed_module is not None:
            if installed_module.version == latest_version:
                self.pushButton.setText(ButtonState.UNINSTALL.value)
                self.buttonState = ButtonState.UNINSTALL

            else:
                self.pushButton.setText(ButtonState.UPDATE.value)
                self.buttonState = ButtonState.UPDATE
        else:
            self.buttonState = ButtonState.INSTALL

    def click_action(self):
        if self.buttonState == ButtonState.INSTALL:
            self.download()
        elif self.buttonState == ButtonState.UPDATE:
            self.update()
        elif self.buttonState == ButtonState.UNINSTALL:
            self.uninstall()
        else:
            pass

    def download(self):
        self.pushButton.setText("installing..")
        self.pushButton.enabled = False

        module = self.module
        url = (self.download_url.replace("<id>", str(module["id"]))) \
            .replace("<latest_vesrsion_id>", str(module["latest_version"]["id"]))
        zip_path = os.path.join(user_folder_path, module["name"])
        urllib.request.urlretrieve(url, zip_path)

        install(module, zip_path)
        logger.info("installed " + self.name + " module")

        self.pushButton.setText(ButtonState.UNINSTALL.value)
        self.buttonState = ButtonState.UNINSTALL

    def uninstall(self):
        uninstall(self.module)
        logger.info("uninstalled " + self.name + " module")
        self.pushButton.setText(ButtonState.INSTALL.value)
        self.buttonState = ButtonState.INSTALL

    def update(self):
        update(self.module)
        logger.info("updated " + self.name + " module")
        self.pushButton.setText(ButtonState.UNINSTALL.value)
        self.buttonState = ButtonState.UNINSTALL
