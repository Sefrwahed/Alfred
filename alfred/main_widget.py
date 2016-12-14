# Qt imports
from PyQt5.QtCore import Qt, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QDialog

from .ui.widget_ui import Ui_Dialog


class MainWidget(QDialog, Ui_Dialog):
    text_changed = pyqtSignal('QString')

    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)

        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)

        self.last_text = ''
        self.lineEdit.returnPressed.connect(self.send_text)

    @pyqtSlot()
    def send_text(self):
        msg = self.lineEdit.text()
        if msg != '' and self.last_text != msg:
            self.text_changed.emit(msg)
            self.last_text = msg
