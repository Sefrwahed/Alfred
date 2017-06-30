from .a_component import AComponent


class AImage(AComponent):
    def __init__(self, source, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.attrs["src"] = source

    def tagname(self):
        return "img"