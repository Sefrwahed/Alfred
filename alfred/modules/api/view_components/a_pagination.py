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
		self.attrs["child"] = str(len(attributes))
		li = AList(html_attributes={"class":"waves-effect" , "id":"0"})
		a = AHref(url="#!", link="")
		i = AIcon(icon = "chevron_left")
		i.attrs['class'] = "material-icons"
		a.add_to_content(i)
		li.add_to_content(a)
		self.add_to_content(li)

		counter = 1
		for attribute in attributes:
			a = AHref(url="#!", link=attribute)
			if counter == 1:
				li = AList(html_attributes={"class":"waves-effect", "id":str(counter)})
				counter += 1
			else:
				li = AList(html_attributes={"class":"waves-effect", "id":str(counter)})
				counter += 1
			li.add_to_content(a)
			self.add_to_content(li)

		li = AList(html_attributes={"class":"waves-effect", "id":str(-1)})
		a = AHref(url="#!", link="")
		i = AIcon(icon = "chevron_right")
		i.attrs['class'] = "material-icons"
		a.add_to_content(i)
		li.add_to_content(a)
		self.add_to_content(li)


	def tagname(self):
		return "ul"
