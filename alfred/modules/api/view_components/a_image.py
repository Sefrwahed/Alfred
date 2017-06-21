from .a_component import AComponent

class AImage(AComponent):
    def __init__(self, html_attributes={},*args, **kwargs):
        super().__init__(*args, **kwargs)
        for i in html_attributes:
	        self.attrs[i] = html_attributes[i]

    def tagname(self):
        return "img"
