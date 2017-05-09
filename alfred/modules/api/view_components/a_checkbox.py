from .a_composite_component import ACompositeComponent
from .a_label import ALabel
from .a_input import AInput
from .a_paragraph import AParagraph


class ACheckbox(ACompositeComponent):
    def __init__(self, label_text, state, id, *args, **kwargs):
        input = AInput(type="checkbox")
        input.attrs["id"] = f"item_{id}"
        input.attrs["data-id"] = id
        if state:
            input.attrs["checked"] = "checked"
        text = ALabel(label_text, **{"for": f"item_{id}"})
        self.root_component = AParagraph(input, text, *args)
