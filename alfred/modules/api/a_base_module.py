import os
import threading

from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot
from jinja2 import Environment, FileSystemLoader

from alfred.settings import Settings
import alfred.modules.api.a_module_globals as amg


class ABaseModule(QThread):
    signal_view_changed = pyqtSignal(list)

    def __init__(self, module_info, entities=''):
        QThread.__init__(self)
        self.components = []
        self.module_info = module_info

        settings_path = os.path.join(self.module_info.root(),
                                     'data', 'settings.json')
        self.settings = Settings(settings_path)

        amg.module_db_path = os.path.join(self.module_info.root(),
                                      'data', 'db.sqlite')

        self.template_env = Environment(
            loader=FileSystemLoader(
                os.path.join(
                    self.module_info.root(),
                    self.module_info.package_name(),
                    'views'
                )
            ),
            autoescape=False
        )

        self.html = ''
        self.callback_method = None
        self.callback_method_args = []

    def run(self):
        if self.callback_method is None:
            self.callback()
            self.construct_view()
            self.populate_view()
        else:
            self.callback_method(*self.callback_method_args)

    def callback(self):
        pass

    def add_component(self, component):
        self.components.append(component)

    def construct_view(self):
        pass

    def render_template(self, t_name, **kwargs):
        t = self.template_env.get_template(t_name)
        html = t.render(**kwargs)
        self.add_component(html)

    def populate_view(self):
        self.signal_view_changed.emit(self.components)

    @pyqtSlot(str, str, dict)
    def event_triggered(self, element_id, event, attrs):
        callback_method = 'on_{}_{}'.format(element_id, event)
        if hasattr(self, callback_method):
            self.callback_method = getattr(self, callback_method)
            self.callback_method_args = [attrs]
            self.start()

    @pyqtSlot(str, dict)
    def form_submitted(self, form_id, form_vals):
        callback_method = 'on_{}_submitted'.format(form_id)
        if hasattr(self, callback_method):
            self.callback_method = getattr(self, callback_method)
            self.callback_method_args = [form_vals]
            self.start()