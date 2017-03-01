import json
import os
from abc import ABC, abstractmethod

from alfred.settings import Settings
from alfred.alfred_globals import user_folder_path

class ABaseModule(ABC):
    def __init__(self, module_info, entities=''):
        self.components = []
        self.module_info = module_info
        self.settings = Settings(os.path.join(
            user_folder_path, 'settings', f'{module_info.name}.json'))

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

