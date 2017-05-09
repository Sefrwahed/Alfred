from .a_component import AComponent

class ARow(AComponent):
    def __init__(self, *args, **kwargs):
        self.attrs["class"] = "row"
        super().__init__(*args, **kwargs)

    def tagname(self):
        return "div"