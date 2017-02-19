# Qt imports
from PyQt5.QtCore import Qt, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QMainWindow

from .ui.window_ui import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    text_changed = pyqtSignal('QString')

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)


    @pyqtSlot()
    def setModules(self):
        pass
