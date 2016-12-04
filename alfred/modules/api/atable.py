from .acomponent import AComponent


class ATable(AComponent):
    def __init__(self, table=[[]], header=[],
                 style_class='', cell_style_class='',
                 header_cells_style_class=''):
        super().__init__()
        self.update_properties(table=table, header=header,
                               style_class=style_class,
                               cell_style_class=cell_style_class,
                               header_cells_style_class=header_cells_style_class)

    @classmethod
    def template_name(self):
        return "table.html"

    def update_properties(self, **kwargs):
        self.template_data.update(kwargs)

    def table(self, table):
        self.template_data['table'] = table

    def header(self, header):
        self.template_data['header'] = header

    def style_class(self, style_class):
        self.template_data['style_class'] = style_class

    def cell_style_class(self, cell_style_class):
        self.template_data['cell_style_class'] = cell_style_class

    def header_cells_style_class(self, header_cells_style_class):
        self.template_data['header_cells_style_class'] = header_cells_style_class
