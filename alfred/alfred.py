# PyQt imports
from PyQt5.QtCore import QCoreApplication, pyqtSlot
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QSystemTrayIcon, QAction, QMenu

# Local imports
from . import logger
from .main_widget import MainWidget
from .modules.api.base_module import BaseModule


class Alfred(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.init_tray_icon()
        self.main_widget = MainWidget()
        self.main_widget.text_changed.connect(self.process_text)

    def init_tray_icon(self):
        self.restore_action = QAction("Show Main Window", self)
        self.quit_action = QAction("Quit", self)

        self.restore_action.triggered.connect(self.show)
        self.quit_action.triggered.connect(QCoreApplication.instance().quit)

        tray_icon_menu = QMenu(self)
        tray_icon_menu.addAction(self.restore_action)
        tray_icon_menu.addSeparator()
        tray_icon_menu.addAction(self.quit_action)

        self.tray_icon = QSystemTrayIcon(QIcon(':/icon_heart'), self)
        self.tray_icon.setContextMenu(tray_icon_menu)
        self.tray_icon.show()
        self.tray_icon.showMessage('Alfred', 'I am alive',
                                   QSystemTrayIcon.Information, 5000)
        self.tray_icon.activated.connect(self.tray_icon_activated)

    def tray_icon_activated(self, reason):
        if(reason == QSystemTrayIcon.Trigger):
            self.main_widget.showFullScreen()

    @pyqtSlot('QString')
    def process_text(self, text):
        # intent = nlp(text)
        module = BaseModule({"time": "now"})
        module_layout = module.main_layout()
        self.main_widget.set_viewport_layout(module_layout)
        module.start()

    def nlp(self, msg):
        logger.info('receiving msg from user now')
        logger.info(msg)
        return "BaseModule"
