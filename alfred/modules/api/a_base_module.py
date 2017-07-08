import os

from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot
from jinja2 import Environment, FileSystemLoader

from alfred import Logger
from alfred.settings import Settings
import alfred.modules.api.a_module_globals as amg


class ABaseModule(QThread):
    signal_view_changed = pyqtSignal(list)
    signal_append_content = pyqtSignal(str, str)
    signal_remove_component = pyqtSignal(str)

    def __init__(self, module_info, entities):
        QThread.__init__(self)
        self.components = []
        self.module_info = module_info

        data_dir_path = os.path.join(self.module_info.root(), 'data')
        amg.module_db_path = os.path.join(data_dir_path, 'db.sqlite')

        if not os.path.isdir(data_dir_path):
            os.makedirs(data_dir_path)
            Logger().info('Created new directory ' + data_dir_path)

        settings_path = os.path.join(data_dir_path, 'settings.json')
        self.settings = Settings(settings_path)

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

        self.entities = entities

    def run(self):
        try:
            if self.callback_method is None:
                self.callback()
                self.construct_view()
                self.signal_view_changed.emit(self.components)
            else:
                self.callback_method(*self.callback_method_args)
        except Exception as e:
            print(e)

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

    def remove_component_by_id(self, component_id):
        self.signal_remove_component.emit(component_id)

    def remove_component(self, component):
        if hasattr(component, "root_component"):
            self.remove_component_by_id(component.root_component.dom_id)
        else:
            self.remove_component_by_id(component.dom_id)

    def append_to(self, parent_component, child_component):
        if hasattr(parent_component, "root_component"):
            self.signal_append_content.emit(parent_component.root_component.dom_id, str(child_component))
        else:
            self.signal_append_content.emit(parent_component.dom_id, str(child_component))

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