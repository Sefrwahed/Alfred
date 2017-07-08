import string
from enum import Enum


# Qt imports
from PyQt5.QtWidgets import QGroupBox
from PyQt5.QtCore import pyqtSlot, pyqtSignal

from .ui.moduleGroupBox_ui import Ui_GroupBox
from alfred.modules import ModuleInfo
from alfred.modules import ModuleManager


class InstallButtonState(Enum):
    UNINSTALL = "Uninstall"
    INSTALL = "Install"


class UpdateButtonState(Enum):
    UPDATE = "Update"
    UPTODATE = "UpToDate"


class ModuleGroupBox(QGroupBox, Ui_GroupBox):
    signal_install = pyqtSignal(dict)
    signal_uninstall = pyqtSignal(int)
    signal_update = pyqtSignal(dict)

    def __init__(self, module_info):
        QGroupBox.__init__(self)
        self.setupUi(self)
        self.installButtonState = None
        self.name = None

        self.module = module_info
        self.set_data()

        self.pushButton_install.clicked.connect(self.install_click_action)
        self.pushButton_update.clicked.connect(self.update_click_action)

    def set_data(self):
        self.name = self.module["name"]
        self.name = self.name.replace('-', ' ')
        self.name = string.capwords(self.name)

        latest_version = self.module["latest_version"]["number"]

        self.labelName_2.setText(self.name)
        self.labelDesc_2.setText(self.module["description"])
        self.labelLicense_2.setText(self.module["license"])
        self.labelVersion_2.setText("Latest version: "+ latest_version)

        installed_module = ModuleInfo.find_by_id(self.module["id"])

        if installed_module is not None:
            self.labelInstalledVersion_2.setText("Current version: "+ installed_module.version)
            self.installButtonState = InstallButtonState.UNINSTALL
            self.pushButton_update.show()
            self.pushButton_install.setText(InstallButtonState.UNINSTALL.value)

            if installed_module.version == latest_version:
                self.pushButton_update.setText(UpdateButtonState.UPTODATE.value)
                self.pushButton_update.hide()

            else:
                self.pushButton_update.setText(UpdateButtonState.UPDATE.value)
                self.pushButton_update.show()

        else:
            self.labelInstalledVersion_2.setText("")
            self.installButtonState = InstallButtonState.INSTALL
            self.pushButton_update.hide()
            self.pushButton_install.setText(InstallButtonState.INSTALL.value)

    def install_click_action(self):
        if self.installButtonState == InstallButtonState.INSTALL:
            self.pushButton_install.setText("installing..")
            self.pushButton_install.enabled = False
            self.signal_install.emit(self.module)

        elif self.installButtonState == InstallButtonState.UNINSTALL:
            self.pushButton_install.setText("uninstalling..")
            self.pushButton_install.enabled = False
            self.signal_uninstall.emit(self.module["id"])

    def update_click_action(self):
        self.pushButton_update.setText("updating..")
        self.pushButton_update.enabled = False
        self.signal_update.emit(self.module)

    @pyqtSlot(int)
    def installed_or_updated(self, id):
        if int(self.module["id"]) == id:
            self.pushButton_install.setText(InstallButtonState.UNINSTALL.value)
            self.pushButton_update.setText(UpdateButtonState.UPTODATE.value)
            self.labelInstalledVersion_2.setText("Current version: "+ self.module["latest_version"]["number"])
            self.installButtonState = InstallButtonState.UNINSTALL
        else:
            self.pushButton_install.setEnabled(True)
            self.pushButton_update.setEnabled(True)

    @pyqtSlot(int)
    def uninstalled(self, mod_id):
        if int(self.module["id"]) == mod_id:
            self.pushButton_update.hide()
            if not(ModuleManager.instance().update_flag):
                self.pushButton_install.setText(InstallButtonState.INSTALL.value)
            self.pushButton_update.enabled = False
            self.labelInstalledVersion_2.setText("")
            self.installButtonState = InstallButtonState.INSTALL

    @pyqtSlot(int)
    def disable_btns(self, id):
        if not(int(self.module["id"]) == id):
            self.pushButton_install.setEnabled(False)
            self.pushButton_update.setEnabled(False)

