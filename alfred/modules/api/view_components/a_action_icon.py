from alfred.modules.api.view_components.a_icon import AIcon


class AActionIcon(AIcon):
    def __init__(self, icon, color, data_action, data_id, size='small'):
        super().__init__(icon, color, "right", size=size, **{"data-id": data_id, "data-action": data_action})