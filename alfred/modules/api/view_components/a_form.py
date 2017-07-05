from alfred.modules.api.view_components.a_button import AButton
from .a_component import AComponent
from .a_icon import AIcon


class AForm(AComponent):
    def __init__(self, floating_submit_button=True, submit_icon="send", *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.content.append(AButton(floating_submit_button, AIcon(submit_icon), type="submit"))

    def tagname(self):
        return "form"