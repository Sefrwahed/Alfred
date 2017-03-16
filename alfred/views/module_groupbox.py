import string
from enum import Enum


# Qt imports
from PyQt5.QtWidgets import QGroupBox
from PyQt5.QtCore import pyqtSlot, pyqtSignal

from .ui.moduleGroupBox_ui import Ui_GroupBox
from alfred.modules import ModuleInfo
from alfred.modules import ModuleManager
from alfred.logger import Logger


class ButtonState(Enum):
    UNINSTALL = "Uninstall"
    INSTALL = "Install"
    UPDATE = "Update"


class ModuleGroupBox(QGroupBox, Ui_GroupBox):
    signal_install = pyqtSignal(dict)
    signal_uninstall = pyqtSignal(int)
    signal_update = pyqtSignal(dict)

    def __init__(self, module_info):
        QGroupBox.__init__(self)
        self.setupUi(self)
        self.buttonState = None
        self.name = None

        self.module = module_info
        self.set_data()

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

        installed_module = ModuleInfo.find_by_id(self.module["id"])
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
            self.pushButton.setText("installing..")
            self.pushButton.enabled = False
            self.signal_install.emit(self.module)

        elif self.buttonState == ButtonState.UPDATE:
            ModuleManager.instance().update(self.module)

        elif self.buttonState == ButtonState.UNINSTALL:
            self.signal_uninstall.emit(self.module["id"])

    @pyqtSlot(int)
    def installed(self, id):
        if int(self.module["id"]) == id:
            self.pushButton.setText(ButtonState.UNINSTALL.value)
            self.buttonState = ButtonState.UNINSTALL

    @pyqtSlot(int)
    def uninstalled(self, id):
        if int(self.module["id"]) == id:
            self.pushButton.setText(ButtonState.INSTALL.value)
            self.buttonState = ButtonState.INSTALL

    # def uninstall(self):
        # logger.info("uninstalled " + self.name + " module")

    # def update(self):
        # logger.info("updated " + self.name + " module")
        # self.pushButton.setText(ButtonState.UNINSTALL.value)
        # self.buttonState = ButtonState.UNINSTALL
