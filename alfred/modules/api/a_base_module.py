from abc import ABC, abstractmethod


class ABaseModule(ABC):
    def __init__(self, entities=""):
        self.components = []

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
