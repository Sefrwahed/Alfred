# Qt imports
from PyQt5.QtWidgets import QApplication

# Python imports
import sys

# Local imports
from alfred.alfred import Alfred


def main():
    try:
        app = QApplication(sys.argv)
        app.setQuitOnLastWindowClosed(False)
        a = Alfred()
        a.hide()
        app.exec_()
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()
