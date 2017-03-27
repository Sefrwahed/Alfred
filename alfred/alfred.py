# PyQt imports
from PyQt5.QtCore import QCoreApplication, pyqtSlot
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QSystemTrayIcon, QAction, QMenu

# Local imports
import sys
import os
from . import alfred_globals as ag
from . import data_rc
from .views import MainWidget
from .views import MainWindow
from .nlp import Classifier
from .modules import ModuleManager
from .modules import ModuleInfo


class Alfred(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.init_tray_icon()

        self.main_widget = MainWidget()
        self.main_widget.text_changed.connect(self.process_text)

        self.main_window = MainWindow()
        self.modules_mgr = ModuleManager.instance()

        self.main_window.signal_list_modules.connect(
            self.modules_mgr.fetch_data
        )

        self.modules_mgr.conn_err.connect(
            self.main_window.handle_connection_error
        )

        self.modules_mgr.data_fetched.connect(self.main_window.list_modules)

    def init_tray_icon(self):
        self.show_widget = QAction("Show Main Widget", self)
        self.restore_action = QAction("Show Main Window", self)
        self.quit_action = QAction("Quit", self)

        self.show_widget.triggered.connect(self.show_main_widget)
        self.restore_action.triggered.connect(self.show_main_window)
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
        if (reason == QSystemTrayIcon.Trigger):
            self.show_main_widget()

    def show_main_widget(self):
        self.main_widget.showFullScreen()

    def show_main_window(self):
        self.main_window.show()

    @pyqtSlot('QString')
    def process_text(self, text):
        module_info = ModuleInfo.find_by_id(Classifier().predict(text))
        if not module_info:
            return

        if module_info.root() in sys.path:
            sys.path.remove(module_info.root())
        sys.path.append(module_info.root())

        package_name = module_info.package_name()
        module = __import__(f'{package_name}.{package_name}',
                            fromlist=package_name)

        ModuleClass = getattr(module, module_info.class_name())

        self.curr_alfred_module = ModuleClass(module_info)

        self.curr_alfred_module.run()

        temp = ag.main_components_env.get_template("base.html")
        html = temp.render(componenets=self.curr_alfred_module.components)
        self.main_widget.webView.page().setHtml(html)
