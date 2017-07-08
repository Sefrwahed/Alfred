# Qt imports
from PyQt5.QtCore import Qt, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QVBoxLayout

from .ui.window_ui import Ui_MainWindow
from .module_groupbox import ModuleGroupBox
from alfred.modules import ModuleManager
from alfred.logger import Logger


class MainWindow(QMainWindow, Ui_MainWindow):
    signal_list_modules = pyqtSignal()

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.setAttribute(Qt.WA_TranslucentBackground, True)

        self.verticalLayout_inner = QVBoxLayout()
        self.modulesManager_tab.setLayout(self.verticalLayout_inner)

        self.pushButtonRetry.clicked.connect(self.showEvent)

    @pyqtSlot(list)
    def list_modules(self, response):
        self.clear_listed_modules()
        for module in response:
            item = ModuleGroupBox(module)
            self.verticalLayout_inner.addWidget(item, alignment=Qt.AlignTop)

            ModuleManager.instance().installation_started.connect(
                item.disable_btns
            )
            ModuleManager.instance().update_started.connect(
                item.disable_btns
            )

            item.signal_install.connect(ModuleManager.instance().download)
            item.signal_update.connect(ModuleManager.instance().update)
            item.signal_uninstall.connect(ModuleManager.instance().uninstall)

            ModuleManager.instance().installation_finished.connect(
                item.installed_or_updated
            )
            ModuleManager.instance().uninstallation_finished.connect(
                item.uninstalled
            )
        self.groupBoxError.hide()

    @pyqtSlot()
    def handle_connection_error(self):
        self.clear_listed_modules()
        self.groupBoxError.show()
        self.labelError.setText("No Internet Connection")

    def showEvent(self, QShowEvent):
        self.labelError.setText("Loading...")
        self.signal_list_modules.emit()

    def clear_listed_modules(self):
        for i in reversed(range(self.verticalLayout_inner.count())):
            self.verticalLayout_inner.itemAt(i).widget().deleteLater()
