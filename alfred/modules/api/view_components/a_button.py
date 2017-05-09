from alfred.modules.api.view_components.a_component import AComponent


class AButton(AComponent):
    def __init__(self, floating=False, *args, **kwargs):
        self.attrs["class"] = "btn"
        if floating:
            self.attrs["class"] += "-floating"
        super().__init__(*args, **kwargs)

    def tagname(self):
        return "button"