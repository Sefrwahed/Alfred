from .a_component import AComponent

class AUnorderedList(AComponent):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

	def tagname(self):
		return "ul"
