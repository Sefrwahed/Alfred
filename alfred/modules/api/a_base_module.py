import os
from abc import ABC, abstractmethod

from alfred.settings import Settings


class ABaseModule(ABC):
    def __init__(self, module_info, entities=''):
        self.components = []
        self.module_info = module_info

        settings_path = os.path.join(self.module_info.root(),
                                     'data', 'settings.json')
        self.settings = Settings(settings_path)

        self.database_path = os.path.join(self.module_info.root(),
                                          'data', 'db.sqlite')

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
