from .a_component import AComponent


class AIcon(AComponent):
    def __init__(self, icon, color="white", float="", size='medium', *args, **kwargs):
        self.attrs["class"] = "material-icons {}-text {} {}".format(color, size, float)
        super().__init__(icon, *args, **kwargs)

    def tagname(self):
        return "i"
