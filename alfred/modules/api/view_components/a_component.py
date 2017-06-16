from abc import ABC, abstractmethod
from alfred import alfred_globals as ag


class AComponent(ABC):
    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls)
        obj.attrs = {}
        return obj

    def __init__(self, *args, **kwargs):
        if hasattr(self, "attrs"):
            default_classes = self.attrs.get("class", "")
            self.attrs = kwargs
            self.attrs["class"] = self.attrs.get("class", "") + " {}".format(default_classes)
        else:
            self.attrs = kwargs
        self.content = list(args)

    def set_content(self, *args):
        self.content = list(args)

    def add_to_content(self, *args):
        self.content.extend(args)

    @abstractmethod
    def tagname(self):
        """
        Return the template name for the current class to be used while
        rendering the corresponding template
        """

    def __str__(self):
        template = ag.main_components_env.get_template("component.html")
        return template.render(
            tagname=self.tagname(),
            attrs=self.attrs,
            content=self.content
        )
