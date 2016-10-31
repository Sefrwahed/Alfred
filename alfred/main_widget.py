# Qt imports
from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QDialog
from .ui.widget_ui import Ui_Dialog


class MainWidget(QDialog, Ui_Dialog):
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
