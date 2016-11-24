# Qt imports
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import pyqtSlot

from PyQt5.QtWidgets import QDialog
from .ui.widget_ui import Ui_Dialog
from . import logger

class MainWidget(QDialog, Ui_Dialog):
    text_changed = pyqtSignal('QString')

    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)

        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        # self.setAttribute(Qt.WA_NoSystemBackground)
        # self.setAttribute(Qt.WA_PaintOnScreen)
        # self.setAttribute(Qt.WA_TransparentForMouseEvents)

        # pal = QPalette()
        # pal.setBrush(QPalette.Window, QColor(0, 0, 0, 220))
        # frame.setPalette(pal)
        # frame.setAutoFillBackground(True)

        self.last_text = ''
        self.lineEdit.returnPressed.connect(self.send_text)

    @pyqtSlot()
    def send_text(self):
        msg = self.lineEdit.text()
        if msg != '' and self.last_text != msg:
            self.text_changed.emit(msg)
            self.last_text = msg

