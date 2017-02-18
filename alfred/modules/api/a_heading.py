from .a_component import AComponent


class AHeading(AComponent):
    def __init__(self, size, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.size = size

    def tagname(self):
        return "h{}".format(self.size)
