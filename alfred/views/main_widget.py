import json

# PyQt imports
from PyQt5.QtCore import Qt, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWebChannel import QWebChannel

# Local includes
from .ui.widget_ui import Ui_Dialog
from alfred import data_rc
import alfred.alfred_globals as ag
from alfred.modules.api.view_components import ARow, AColumn, ACard, AHeading


class MainWidget(QDialog, Ui_Dialog):
    text_changed = pyqtSignal('QString')
    def __init__(self, bridge_obj):
        QDialog.__init__(self)
        self.setupUi(self)

        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)

        self.lineEdit.returnPressed.connect(self.send_text)

        self.channel = QWebChannel(self.webView.page())
        self.webView.page().setWebChannel(self.channel)
        self.bridge_obj = bridge_obj
        self.channel.registerObject("web_bridge", bridge_obj)

    def clear_view(self):
        self.webView.page().setHtml("")

    def set_status_icon_busy(self, busy):
        if busy:
            self.bot_status_icon.page().runJavaScript("document.getElementById('inner').style.width = '0px';")
        else:
            self.bot_status_icon.page().runJavaScript("document.getElementById('inner').style.width = '20px';")

    def show_busy_state_widget(self):
        self.show_special_widget("Please wait...", "Alfred is busy learning at the moment :D")

    def show_module_running_widget(self, module_name):
        self.show_special_widget("Module is running, Please wait...", "{} module is predicted".format(module_name.capitalize()))

    def show_no_modules_view(self):
        self.show_special_widget("Please install some modules", "No modules found :(")

    def show_special_widget(self, title, content, color=''):
        temp = ag.main_components_env.get_template("widgets.html")
        components = [ARow(AColumn(12, ACard(title, AHeading(3, content,color=color))))]
        html = temp.render(componenets=components)
        self.webView.page().setHtml(html)

    @pyqtSlot()
    def send_text(self):
        msg = self.lineEdit.text()
        if msg != '':
            self.text_changed.emit(msg)
            self.last_text = msg

    @pyqtSlot(list)
    def set_widget_view(self, components):
        temp = ag.main_components_env.get_template("widgets.html")
        html = temp.render(componenets=components)
        # print(html)
        self.webView.page().setHtml(html)

    @pyqtSlot(list)
    def set_view(self, components):
        temp = ag.main_components_env.get_template("base.html")
        html = temp.render(componenets=components)
        # print(html)
        self.webView.page().setHtml(html)

    @pyqtSlot(str)
    def remove_component(self, dom_id):
        js = "jQuery('#{}').fadeOut(function(){{ jQuery(this).remove() }});".format(dom_id)
        # print(js)
        self.webView.page().runJavaScript(js)

    @pyqtSlot(str, str)
    def append_content(self, parent_dom_id, element_html):
        js = "jQuery('{}').prependTo('#{}').hide().fadeIn();".format(("".join(element_html.splitlines())).replace("'", ""), parent_dom_id)
        # print(js)
        self.webView.page().runJavaScript(js)