from .a_component import AComponent


class ADivider(AComponent):
    def __init__(self, *args, **kwargs):
        self.attrs["class"] = "divider"
        super().__init__(*args, **kwargs)

    def tagname(self):
        return "div"