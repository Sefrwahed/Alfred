from .a_component import AComponent


class AParagraph(AComponent):
    def tagname(self):
        return "p"