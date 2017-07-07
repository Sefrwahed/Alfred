# Python builtins imports
import sys, json, os

from PyQt5.QtCore import QCoreApplication, pyqtSlot, Qt
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QMainWindow, QSystemTrayIcon, QAction, QMenu, QSplashScreen, QInputDialog


from alfred.nlp.parser import Parser
from .modules import ModuleInfo
from .modules import ModuleManager
from .nlp import Classifier
from .utils import WebBridge
from .widget_manager import WidgetManager

from .views import MainWidget
from .views import MainWindow
from alfred.logger import Logger


class Alfred(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.show_splash()
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

        self.modules_mgr.signal_train.connect(
            Classifier().train
        )

        Classifier().train_thread.finished.connect(
            self.show_widgets_if_visible
        )

        self.modules_mgr.data_fetched.connect(self.main_window.list_modules)
        self.curr_module = None
        self.widget_man = WidgetManager(self.main_widget)

        self.curr_sentence = ''

        self.web_bridge.signal_wrong_module.connect(self.add_new_sentence)

    def show_splash(self):
        image = QPixmap(':/loading_image')
        splash = QSplashScreen(image)
        splash.setAttribute(Qt.WA_DeleteOnClose)
        splash.setMask(image.mask())
        splash.show()

        QCoreApplication.processEvents()
        Parser([])

        splash.finish(self)

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
        self.main_widget.lineEdit.setText("")
        if Classifier().train_thread.isRunning():
            self.main_widget.set_status_icon_busy(True)
            self.main_widget.show_busy_state_widget()
            self.main_widget.showFullScreen()
        else:
            self.main_widget.clear_view()
            
            if self.modules_mgr.modules_count == 0:
                self.main_widget.show_no_modules_view()
            else:
                self.widget_man.prepare_widgets()

            self.main_widget.showFullScreen()

    def show_widgets_if_visible(self):
        if self.main_widget.isVisible():
            self.widget_man.prepare_widgets()

    def show_main_window(self):
        self.main_window.show()

    @pyqtSlot('QString')
    def process_text(self, text):
        if Classifier().train_thread.isRunning():
            self.main_widget.show_busy_state_widget()
            return 

        self.curr_sentence = text
        self.main_widget.set_status_icon_busy(True)

        module_id = Classifier().predict(text)
        module_info = ModuleInfo.find_by_id(module_id)

        if not module_info:
            return

        self.main_widget.show_module_running_widget(module_info.name)

        self.set_module(module_info)

        self.main_widget.set_status_icon_busy(False)

    @pyqtSlot()
    def add_new_sentence(self):
        self.main_widget.hide()
        modules = dict(map(lambda m: (m.name, m), ModuleInfo.all()))
        item, ok = QInputDialog.getItem(self, self.curr_sentence, "Select Module:",
                                     modules.keys(), 0, False);
        print(item, ok)

        mi = modules[item]
        if ok and self.curr_module.module_info.id != mi.id:
            sentences = []

            with open(mi.extra_training_sentences_json_file_path(), 'r+') as extra_train_file:
                sentences = json.load(extra_train_file)
                sentences.append(self.curr_sentence)

            with open(mi.extra_training_sentences_json_file_path(), 'w') as extra_train_file:
                extra_train_file.write(json.dumps(sentences))
                extra_train_file.truncate()

            Classifier().train()

            self.show_main_widget()
        else:
            self.main_widget.showFullScreen()
            self.main_widget.lineEdit.setText(self.curr_sentence)

    def set_module(self, module_info):
        if module_info.root() in sys.path:
            sys.path.remove(module_info.root())
        sys.path.append(module_info.root())

        package_name = module_info.package_name()
        module = __import__('{}.{}'.format(package_name, package_name),
                            fromlist=package_name)

        if self.curr_module is not None:
            self.web_bridge.signal_event_triggered.disconnect(self.curr_module.event_triggered)
            self.web_bridge.signal_form_submitted.disconnect(self.curr_module.form_submitted)

        try:
            needed_entities = module_info.needed_entities()
            Parser([]).set_entities_types(needed_entities)
            entities_list = Parser([]).parse(text)
            Logger().info("Extracted Entities are {}".format(entities_list))
        except:
            entities_list = {}

        self.curr_module = getattr(
            module, module_info.class_name()
        )(module_info, entities_list)

        self.curr_module.signal_view_changed.connect(self.main_widget.set_view)

        self.curr_module.signal_remove_component.connect(self.main_widget.remove_component)
        self.curr_module.signal_append_content.connect(self.main_widget.append_content)

        self.web_bridge.signal_event_triggered.connect(self.curr_module.event_triggered)
        self.web_bridge.signal_form_submitted.connect(self.curr_module.form_submitted)

        self.curr_module.start()

