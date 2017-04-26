from abc import ABC


class ACompositeComponent(ABC):

    def set_root_component(self, comp):
        self.root_component = comp

    def add_to_content(self, *args):
        self.root_component.add_to_content(*args)

    def __str__(self):
        return self.root_component.__str__()
