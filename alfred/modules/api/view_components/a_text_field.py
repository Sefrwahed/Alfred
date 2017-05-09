from .a_composite_component import ACompositeComponent
from .a_icon import AIcon
from .a_input import AInput
from .a_column import AColumn
from .a_label import ALabel


class ATextField(ACompositeComponent):
    def __init__(self, name, label_text, icon_prefix=""):
        icon = ""
        input = AInput(type="text", name=name, id=name)
        label = ALabel(label_text, **{"for": name})
        if icon_prefix != "":
            icon = AIcon(icon_prefix, **{"class": "prefix"})

        self.root_component = AColumn(12, icon, input, label, **{"class":"input-field"})