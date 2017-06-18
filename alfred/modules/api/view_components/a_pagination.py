from .a_list import AList
from .a_unordered_list import AUnorderedList
from .a_component import AComponent
from .a_href import AHref
from .a_icon import AIcon
from .a_script import AScript

class APagination(AComponent):
	def __init__(self, attributes=[],*args,**kwargs):
		super().__init__(*args, **kwargs)
		self.attrs["class"] = "pagination"

		#a = AHref(url="#!", link = AScript(src="/home/mahmoudrizk/Desktop/my_desktop/Alfred/alfred/resources/js/a_pagination.js") )
		#li = AList(class_attribute="waves-effect")
		#li.add_to_content(a)
		#self.add_to_content(AScript(src="/home/mahmoudrizk/Desktop/my_desktop/Alfred/alfred/resources/js/a_pagination.js"))


		li = AList(class_attribute="disabled")
		a = AHref(url="#!", link="")
		i = AIcon(icon = "chevron_left")
		i.attrs['class'] = "material-icons"
		a.add_to_content(i)
		li.add_to_content(a)
		self.add_to_content(li)

		counter = 0
		for attribute in attributes:
			a = AHref(url="#!", link=attribute)
			if counter == 0:
				li = AList(class_attribute="active")
				counter = 1
			else:
				li = AList(class_attribute="waves-effect")
			li.add_to_content(a)
			self.add_to_content(li)

		li = AList(class_attribute="waves-effect")
		a = AHref(url="#!", link="")
		i = AIcon(icon = "chevron_right")
		i.attrs['class'] = "material-icons"
		a.add_to_content(i)
		li.add_to_content(a)
		self.add_to_content(li)


	def tagname(self):
		return "ul"
