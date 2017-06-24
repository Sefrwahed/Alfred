from .a_composite_component import ACompositeComponent
from .a_label import ALabel
from .a_input import AInput
from .a_paragraph import AParagraph


class ACheckbox(ACompositeComponent):
    def __init__(self, label_text, state, *args, **kwargs):
        input = AInput(type="checkbox")

        if kwargs.get("id", "") != "":
            input.attrs["id"] = kwargs["id"]

        self.dom_id = input.attrs["id"]

        if state:
            input.attrs["checked"] = "checked"
        text = ALabel(label_text, **{"for": input.attrs["id"]})
        self.root_component = AParagraph(input, text, *args)
