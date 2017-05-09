from .a_component import AComponent

class AColumn(AComponent):
    def __init__(self, size, *args, **kwargs):
        self.attrs["class"] = f"col s{size}"
        super().__init__(*args, **kwargs)

    def tagname(self):
        return "div"