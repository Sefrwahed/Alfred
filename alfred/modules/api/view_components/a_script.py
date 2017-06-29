from .a_component import AComponent

class AScript(AComponent):
    def __init__(self, src, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.attrs['type'] = "text/javascript"
        self.attrs['src'] = src
        del self.attrs['class']
        self.add_to_content(self.insert_js_to_html())

    def insert_js_to_html(self):
        try:
            js_file = open(self.attrs['src'])
        except:
            return ""
        js_code = js_file.read()
        html_code = ""

        for i in range(0,len(js_code)):
            if js_code[i] == "/" and js_code[i+1] == "n":
                i = i + 2
            else:
                html_code = html_code + js_code[i]
        del self.attrs['src']
        return html_code

    def tagname(self):
        return "script"
