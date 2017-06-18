# PyQt imports
from PyQt5.QtCore import Qt, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWebChannel import QWebChannel

# Local includes
from .ui.widget_ui import Ui_Dialog
from alfred import data_rc
import alfred.alfred_globals as ag


class MainWidget(QDialog, Ui_Dialog):
    text_changed = pyqtSignal('QString')

    def __init__(self, bridge_obj):
        QDialog.__init__(self)
        self.setupUi(self)

        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)

        self.last_text = ''
        self.lineEdit.returnPressed.connect(self.send_text)

        self.channel = QWebChannel(self.webView.page())
        self.webView.page().setWebChannel(self.channel)

        self.channel.registerObject("web_bridge", bridge_obj)

    @pyqtSlot()
    def send_text(self):
        msg = self.lineEdit.text()
        if msg != '' and self.last_text != msg:
            self.text_changed.emit(msg)
            self.last_text = msg

    @pyqtSlot(list)
    def set_view(self, components):
        temp = ag.main_components_env.get_template("base.html")
        html = temp.render(componenets=components)
        print(html) ##Debug
        self.webView.page().setHtml(html)
