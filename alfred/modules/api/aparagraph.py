from .acomponent import AComponent

class AParagraph(AComponent):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def tagname(self):
        return "p"