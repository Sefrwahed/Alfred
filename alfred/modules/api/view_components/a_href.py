from .a_component import AComponent

class AHref(AComponent):
    def __init__(self, url, link, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.attrs['href'] = url
        self.add_to_content(link)
        del self.attrs['class']

    def tagname(self):
        return "a"
