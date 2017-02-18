# PyQt imports
from PyQt5.QtCore import QCoreApplication, pyqtSlot
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QSystemTrayIcon, QAction, QMenu

# Local imports
import imp
import os
import sys
from . import alfred_globals as ag
from . import logger
from .main_widget import MainWidget


class Alfred(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.init_tray_icon()
        self.main_widget = MainWidget()
        self.main_widget.text_changed.connect(self.process_text)

    def init_tray_icon(self):
        self.show_widget = QAction("Show Main Widget", self)
        self.restore_action = QAction("Show Main Window", self)
        self.quit_action = QAction("Quit", self)

        self.show_widget.triggered.connect(self.show_main_widget)
        self.restore_action.triggered.connect(self.show)
        self.quit_action.triggered.connect(QCoreApplication.instance().quit)

        tray_icon_menu = QMenu(self)
        tray_icon_menu.addAction(self.show_widget)
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
            self.show_main_widget()

    def show_main_widget(self):
        self.main_widget.showFullScreen()

    @pyqtSlot('QString')
    def process_text(self, text):
        module_info = self.nlp(text)

        print(sys.path)
        mod = imp.load_source(
            module_info[1],
            os.path.join(ag.modules_folder_path, module_info[0])
        )

        self.curr_alfred_module = getattr(mod, module_info[2])()

        self.curr_alfred_module.run()

        temp = ag.main_components_env.get_template("base.html")
        html = temp.render(componenets=self.curr_alfred_module.components)
        self.main_widget.webView.page().setHtml(html)

    def nlp(self, msg):
        logger.info('receiving msg from user now')
        logger.info(msg)
        return [
            "github.com/Sefrwahed/alfred-weather/alfred-weather.py",
            "alfred-weather.py",
            "AlfredWeather"
        ]
