import json
import os


class Settings():
    def __init__(self, settings_path):
        self.settings_path = settings_path
        self.settings_dict = {}
        self.reload()

    def __getitem__(self, key):
        return self.settings_dict[key]

    def __setitem__(self, key, value):
        self.settings_dict[key] = value

    def reload(self):
        if not (os.path.exists(self.settings_path) and
                    os.path.isfile(self.settings_path)):
            self.commit()

        with open(self.settings_path, 'r') as f:
            self.settings_dict = json.loads(f.read())

    def commit(self):
        dir = os.path.abspath(os.path.dirname(self.settings_path))
        if not os.path.exists(dir):
            os.mkdir(dir)

        with open(self.settings_path, 'w') as f:
            f.writelines(json.dumps(self.settings_dict))
