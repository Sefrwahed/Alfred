# Python builtins imports
import sys

from PyQt5.QtCore import QCoreApplication, pyqtSlot
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QSystemTrayIcon, QAction, QMenu

import alfred.nlp.ner_parsers as parsers
from .modules import ModuleInfo
from .modules import ModuleManager
from .nlp import Classifier
from .utils import WebBridge
from .views import MainWidget
from .views import MainWindow


class Alfred(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.init_tray_icon()

        self.web_bridge = WebBridge()
        self.main_widget = MainWidget(self.web_bridge)
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
        self.curr_module = None

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
        if reason == QSystemTrayIcon.Trigger:
            self.show_main_widget()

    def show_main_widget(self):
        self.main_widget.showFullScreen()

    def show_main_window(self):
        self.main_window.show()

    @pyqtSlot('QString')
    def process_text(self, text):
        preprocessed_text = self.preprocess_text(text)
        module_info = ModuleInfo.find_by_id(Classifier().predict(preprocessed_text))

        if not module_info:
            return

        if module_info.root() in sys.path:
            sys.path.remove(module_info.root())
        sys.path.append(module_info.root())

        package_name = module_info.package_name()
        module = __import__('{}.{}'.format(package_name, package_name),
                            fromlist=package_name)

        if self.curr_module is not None:
            self.web_bridge.signal_event_triggered.disconnect(self.curr_module.event_triggered)

        self.curr_module = getattr(
            module, module_info.class_name()
        )(module_info)

        self.curr_module.signal_view_changed.connect(self.main_widget.set_view)
        self.web_bridge.signal_event_triggered.connect(self.curr_module.event_triggered)
        self.web_bridge.signal_form_submitted.connect(self.curr_module.form_submitted)
        self.curr_module.start()

    def preprocess_text(self, text):
        #normalizarion
        #NER
        return parsers.Spacy().getAnnotatedText(text)

