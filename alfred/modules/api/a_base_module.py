import json
import os
from abc import ABC, abstractmethod


class ABaseModule(ABC):
    def __init__(self, module_info, entities=''):
        self.components = []
        self.module_info = module_info
        self.settings = self.load_settings()

    def run(self):
        self.callback()
        self.construct_view()

    @abstractmethod
    def callback(self):
        pass

    def add_component(self, component):
        self.components.append(component)

    @abstractmethod
    def construct_view(self):
        pass

    def load_settings(self):
        settings_path = os.path.join(self.module_info.root(), 'settings.json')
        if os.path.exists(settings_path) and os.path.isfile(settings_path):
            with open(settings_path, 'r') as f:
                settings = json.loads(f.read())
        else:
            settings = {}
            self.save_settings()

        return settings

    def save_settings(self):
        settings_path = os.path.join(self.module_info.root(), 'settings.json')
        with open(settings_path, 'w') as f:
            f.writelines(json.dumps(self.settings))
