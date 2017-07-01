from PyQt5.QtCore import QThread
import alfred.modules.api.a_module_globals as amg


class ABaseWidget(QThread):
    def __init__(self):
        QThread.__init__(self)

        self.title = None
        self.image_url = None
        self.content = []
        self.color = ""
        self.title_on_image = False

    def run(self):
        self.callback()
        self.construct_view()

    def callback(self):
        pass

    def construct_view(self):
        pass