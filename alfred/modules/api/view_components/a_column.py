from .a_div import ADiv

class AColumn(ADiv):
    def __init__(self, size, *args, **kwargs):
        self.attrs["class"] = "col s{}".format(size)
        super().__init__(*args, **kwargs)