from .a_list import AList
from .a_unordered_list import AUnorderedList
from .a_divider import ADivider
from .a_span import ASpan
from .a_icon import AIcon
from .a_component import AComponent

"""
##################################################
< FORMAT FOR collapsible_type={} & attributes={} >
----> xxxxx : refers to value sent from user.
##################################################

collapsible_type = {
'class':'xxxxx'
'data-collapsible':'xxxxx'
}

attributes = [{
    'header':{
         'badge':{
            'class':'xxxxx','value':'xxxxx'},
         'icon':'xxxxx',
         'value':'xxxxx'
    },
    'body':{
        'value':'xxxxx'
    }
}]
"""
class ACollapsible(AComponent):

    def __init__(self, collapsible_type={}, attributes=[],*args,**kwargs):
        super().__init__(*args, **kwargs)
        self.background_color =  'N/A'

        if 'class' in collapsible_type:
            self.attrs['class'] = collapsible_type['class']
        else: #Default
            self.attrs['class'] = "collapsible"

        if 'data-collapsible' in collapsible_type:
            self.attrs['data-collapsible'] = collapsible_type['data-collapsible']
        else: ##Default
            self.attrs['data-collapsible'] = "accordion"

        self.attrs['style'] = 'border-top: 0px; border-right: 0px; border-left: 0px; background-color:' + self.background_color + ';'

        for i in range(0,len(attributes)):

            head = ADivider()
            head.attrs['class'] = "collapsible-header"

            if 'badge' in attributes[i]['header']:
                badge = ASpan({'class':attributes[i]['header']['badge']['class']})
                badge.add_to_content(attributes[i]['header']['badge']['value'])
                head.add_to_content(badge)

            if 'icon' in attributes[i]['header']:
                icon = AIcon({'class':"material-icons"})
                icon.add_to_content(attributes[i]['header']['icon'])
                head.add_to_content(icon)

            head.add_to_content(attributes[i]['header']['value'])

            body = ADivider()
            body.attrs['class'] = "collapsible-body"
            body.add_to_content(attributes[i]['body']['value'])

            li = AList()
            li.add_to_content(head)
            li.add_to_content(body)


            self.add_to_content(li)


    def tagname(self):
        return "ul"
