from .a_component import AComponent

class AColumn(AComponent):
    def __init__(self, size, *args, **kwargs):
        self.attrs["class"] = "col s{}".format(size)
        super().__init__(*args, **kwargs)

    def tagname(self):
        return "div"