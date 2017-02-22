# Qt imports
from PyQt5.QtWidgets import QApplication

# Python imports
import sys

# Local imports
from alfred.alfred import Alfred


def main():
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    a = Alfred()
    a.hide()
    app.exec_()


if __name__ == '__main__':
    main()
