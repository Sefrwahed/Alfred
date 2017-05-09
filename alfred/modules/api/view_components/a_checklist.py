from alfred.modules.api.view_components.a_action_icon import AActionIcon
from .a_checkbox import ACheckbox
from .a_composite_component import ACompositeComponent
from .a_paragraph import AParagraph


class AChecklist(ACompositeComponent):
    def __init__(self, items=[], *args, **kwargs):
        super().__init__(*args, **kwargs)
        list_items = list(map(
            lambda x: ACheckbox(x[0], x[1], x[2], AActionIcon("delete", "red", "delete", x[2])),
            items
        ))
        self.root_component = AParagraph(*list_items)

    def add_item(self, item):
        self.root_component.add_to_content(
            ACheckbox(item[0], item[1], item[2], AActionIcon("delete", "red", "delete", item[2]))
        )