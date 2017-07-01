from .a_component import AComponent


class AHeading(AComponent):
    def __init__(self, size, *args, **kwargs):
        self.size = size
        super().__init__(*args, **kwargs)

    def tagname(self):
        return "h{}".format(self.size)
