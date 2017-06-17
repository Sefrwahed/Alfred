from .a_component import AComponent

class AList(AComponent):
	def __init__(self, class_attribute="", *args, **kwargs):
		super().__init__(*args, **kwargs)
		if class_attribute != "":
			self.attrs["class"] = class_attribute
		else:
			pass
	def tagname(self):
		return "li"
