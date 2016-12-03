from .acomponent import AComponent


class AHeader(AComponent):
    def __init__(self, size=1, text=None):
        super().__init__()
        self.size(size)
        self.text(text)

    @classmethod
    def template_name(self):
        return "header.html"

    def size(self, size):
        self.template_data['size'] = size

    def text(self, text):
        self.template_data['text'] = text
