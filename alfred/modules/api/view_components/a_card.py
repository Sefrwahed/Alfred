from .a_composite_component import ACompositeComponent
from .a_span import ASpan
from .a_div import ADiv
from .a_image import AImage


class ACard(ACompositeComponent):
    def __init__(self, title, image_url=None, title_on_image=False, size="", color="", orientation="", *args):
        self.root_component = ADiv()
        self.root_component.attrs["class"] = "card {} {} {}".format(size, color, orientation)

        title_span = ASpan(title)
        title_span.attrs["class"] = "card-title"

        card_content = ADiv()
        card_content.attrs["class"] = "card-content"

        if image_url is not None:

            image = AImage(image_url)
            image_div = ADiv(image)
            image_div.attrs["class"] = "card-image"

            if title_on_image:
                image_div.add_to_content(title_span)
            else:
                card_content.add_to_content(title_span)

            self.root_component.add_to_content(image_div)
        else:
            card_content.add_to_content(title_span)
            
        card_content.add_to_content(*args)
        self.root_component.add_to_content(card_content)

