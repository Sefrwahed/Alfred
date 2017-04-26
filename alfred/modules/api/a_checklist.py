from .a_composite_component import ACompositeComponent
from .a_checkbox import ACheckbox
from .a_paragraph import AParagraph


class AChecklist(ACompositeComponent):
    def __init__(self, items=[], *args, **kwargs):
        super().__init__(*args, **kwargs)
        list_items = list(map(lambda x: ACheckbox(label_text=x[0], state=x[1]), items))
        self.root_component = AParagraph(*list_items)

    def add_item(self, item):
        self.root_component.add_to_content(ACheckbox(label_text=item[0], state=item[1]))