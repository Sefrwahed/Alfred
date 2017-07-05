from .a_div import ADiv

class ARow(ADiv):
    def __init__(self, *args, **kwargs):
        self.attrs["class"] = "row"
        super().__init__(*args, **kwargs)