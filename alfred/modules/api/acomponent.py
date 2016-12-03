from abc import ABC, abstractclassmethod
from alfred import alfred_globals as ag


class AComponent(ABC):
    def __init__(self):
        self.template_data = {}

    @abstractclassmethod
    def template_name(self):
        """
        Return the template name for the current class to be used while
        rendering the corresponding template
        """

    def __str__(self):
        template = ag.main_components_env.get_template(self.template_name())
        return template.render(self.template_data)
