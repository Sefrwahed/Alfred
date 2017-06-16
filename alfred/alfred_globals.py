# Python builtins imports
import os
import sys
import pathlib
import json

# Libs imports
from jinja2 import Environment, FileSystemLoader

# Local imports
from alfred.settings import Settings

APP_NAME = "Alfred"
WIT_TOKEN = "GMCAOZ4HFZ3Q5K7FNOFIQSR6VCM6NA47"

main_components_env = Environment(
    loader=FileSystemLoader(
        [
            os.path.join('alfred', 'modules', 'templates'),
            os.path.join('alfred', 'resources', 'css'),
            os.path.join('alfred', 'resources', 'js')
        ]
    ),
    autoescape=False
)

js_path = os.path.abspath(os.path.join('alfred', 'resources', 'js'))

# Adding api to sys.path
sys.path.extend([os.path.join('alfred', 'modules', 'api')])

user_home_path = os.path.expanduser("~")
user_folder_name = "." + APP_NAME.lower()
user_folder_path = os.path.join(user_home_path, user_folder_name)


def global_file_path(global_file):
    return os.path.join(user_folder_path, global_file)


# Database
db_name = "alfred.db"

# Classifier
clf_file = "classifier.pkl"

# SpaCy
spacy_path = "/usr/local/lib/python3.5/dist-packages/spacy/data/en-1.1.0/"
spacy_ner_path = pathlib.Path(spacy_path + "ner/")
with open(spacy_path + "vocab/tag_map.json", "r") as d:
    spacy_tag_map = json.load(d)
# Log
LOG_FILE = 'log'

# Modules folder
if (not os.path.isdir(user_folder_path)):
    os.makedirs(user_folder_path)

modules_folder_path = os.path.join(user_folder_path, "modules")
sys.path.extend([modules_folder_path])

if (not os.path.isdir(modules_folder_path)):
    os.makedirs(modules_folder_path)

# Modules server
host_url = 'http://alfredhub.herokuapp.com/'
modules_list_url = host_url + 'alfred_modules.json'
modules_download_url = host_url + 'alfred_modules/{id}/versions/{version_id}/download'

settings_path = os.path.join(user_folder_path, 'settings.json')
global_settings = Settings(settings_path)
