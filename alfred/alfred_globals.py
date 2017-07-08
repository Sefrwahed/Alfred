# Python builtins imports
import os, sys, shutil

# Libs imports
from jinja2 import Environment, FileSystemLoader

# Local imports
from alfred.settings import Settings

APP_NAME = "Alfred"

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
tmp_folder_path = os.path.join(user_folder_path, "tmp")

def global_file_path(global_file):
    return os.path.join(user_folder_path, global_file)


# Database
db_name = "alfred.db"

# Classifier
clf_file = "classifier.pkl"

# Log
LOG_FILE = 'log'

# Modules folder
if (not os.path.isdir(user_folder_path)):
    os.makedirs(user_folder_path)

modules_folder_path = os.path.join(user_folder_path, "modules")
sys.path.extend([modules_folder_path])

if (not os.path.isdir(modules_folder_path)):
    os.makedirs(modules_folder_path)

if (not os.path.isdir(tmp_folder_path)):
    os.makedirs(tmp_folder_path)

# nltk data
if (not os.path.isdir(os.path.join(user_home_path, "nltk_data"))):
    shutil.copytree(
        os.path.join(os.path.dirname(__file__), "nltk_data"), 
        os.path.join(user_home_path, "nltk_data")
    )

# Modules server
host_url = 'http://alfredhub.herokuapp.com/'
modules_list_url = host_url + 'alfred_modules.json'
modules_download_url = host_url + 'alfred_modules/{id}/versions/{version_id}/download'

settings_path = os.path.join(user_folder_path, 'settings.json')
global_settings = Settings(settings_path)
