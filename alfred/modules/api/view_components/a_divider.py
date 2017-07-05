from .a_div import ADiv


class ADivider(ADiv):
    def __init__(self, *args, **kwargs):
        self.attrs["class"] = "divider"
        super().__init__(*args, **kwargs)
