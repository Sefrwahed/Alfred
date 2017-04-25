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
        print("run", threading.get_ident())
        if self.callback_method is None:
            self.callback()
            self.construct_view()
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
        self.signal_view_changed.emit([html])

    def get_input_value(self, input_id):
        return self.web_content_helper.get_input_value(input_id)

    @pyqtSlot(str, str)
    def event_triggered(self, element_id, event):
        callback_method = f'on_{element_id}_{event}'
        if hasattr(self, callback_method):
            self.callback_method = getattr(self, callback_method)
            self.start()

    @pyqtSlot(str, str)
    def value_submitted(self, element_id, val):
        print("val sub", threading.get_ident())
        callback_method = f'on_{element_id}_submitted'
        if hasattr(self, callback_method):
            self.callback_method = getattr(self, callback_method)
            self.callback_method_args = [val]
            self.start()
