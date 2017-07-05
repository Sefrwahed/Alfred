import sys, os

from PyQt5.QtCore import QObject, pyqtSlot, QTimer

from .modules import ModuleInfo
from .modules.api.view_components import ARow, AColumn, ACard

import alfred.modules.api.a_module_globals as amg


class WidgetManager(QObject):
    def __init__(self, view_widget):
        QObject.__init__(self)
        self.view_widget = view_widget
        self.widgets_container = None
        self.started_widgets = []
        self.loading_timer = QTimer()
        self.loading_timer.setInterval(500)
        self.loading_timer.setSingleShot(True)
        self.loading_timer.timeout.connect(self.widgets_container_loaded)

    def prepare_widgets(self):
        self.widgets_container = ARow()
        self.view_widget.set_widget_view([self.widgets_container])
        self.loading_timer.start()

    def widgets_container_loaded(self):
        for m in ModuleInfo.all():
            if not os.path.exists(os.path.join(m.root(), m.package_name(), "{}_widget.py".format(m.package_name()))):
                print(os.path.join(m.root(), m.package_name(), "{}_widget.py".format(m.package_name())))
                continue

            amg.module_db_path = os.path.join(m.root(), 'data', 'db.sqlite')

            package_name = m.package_name()

            if m.root() in sys.path:
                sys.path.remove(m.root())
            sys.path.append(m.root())

            module = __import__('{}.{}_widget'.format(package_name, package_name),
                                fromlist=package_name)

            widget_class = getattr(module, "{}Widget".format(m.class_name()), None)
            if widget_class is not None:
                widget = widget_class()
                self.started_widgets.append(widget)
                widget.finished.connect(self.widget_thread_finished)
                widget.start()

    @pyqtSlot()
    def widget_thread_finished(self):
        widget = self.sender()
        if widget.title is not None and widget.content:
            widget_view = AColumn(6, ACard(widget.title, *widget.content,
                                           image_url=widget.image_url, color=widget.color,
                                           title_on_image=widget.title_on_image))
            self.view_widget.append_content(self.widgets_container.dom_id, str(widget_view))