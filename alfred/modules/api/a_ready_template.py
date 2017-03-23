from .a_component import AComponent
from alfred import alfred_globals as ag
from jinja2 import Environment, FileSystemLoader

class AReadyTemplate(AComponent):
    def __init__(self,raw_data,html_path,html_name,*args,**kwargs):
        super().__init__(*args, **kwargs)
        self.raw_data = raw_data  #Data to be populated inside the html file
        self.html_path = html_path
        self.html_name = html_name

    def __str__(self):
        path = Environment(
        loader=FileSystemLoader(self.html_path),
        autoescape=False
        )
        template = path.get_template(self.html_name)
        return template.render(raw_data=self.raw_data)

    def tagname(self):
        pass
