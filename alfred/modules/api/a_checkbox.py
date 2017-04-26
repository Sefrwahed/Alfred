from .a_composite_component import ACompositeComponent
from .a_label import ALabel
from .a_input import AInput
from .a_paragraph import AParagraph


class ACheckbox(ACompositeComponent):
    def __init__(self, label_text, state, *args, **kwargs):
        super().__init__(*args, **kwargs)
        input = AInput(type="checkbox", **kwargs)
        text = ALabel(label_text)
        self.root_component = AParagraph(input, text)
