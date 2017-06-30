from .a_component import AComponent


class AImage(AComponent):
    def __init__(self, source, *args, **kwargs):
        self.attrs["src"] = source
        super().__init__(*args, **kwargs)

    def tagname(self):
        return "img"