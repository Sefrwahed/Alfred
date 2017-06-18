from .a_component import AComponent

class AScript(AComponent):
    def __init__(self, src, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.attrs['type'] = "text/javascript"
        self.attrs['src'] = src
        del self.attrs['class']
        #self.add_to_content("function update_view(){var x = document.getElementsByClassName(\"active\");x[0].className = \"waves-effect\"}")
    def tagname(self):
        return "script"
