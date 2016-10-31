# Qt imports
from PyQt5.QtWidgets import QApplication

# Python imports
import sys

# Local imports
from alfred.alfred import Alfred

app = QApplication(sys.argv)
app.setQuitOnLastWindowClosed(False)
a = Alfred()
a.hide()
app.exec_()
