from jinja2 import Environment, FileSystemLoader
import os
import sys

from alfred.settings import Settings

APP_NAME = "Alfred"
WIT_TOKEN = "GMCAOZ4HFZ3Q5K7FNOFIQSR6VCM6NA47"

main_components_env = Environment(
    loader=FileSystemLoader(os.path.join('alfred', 'modules', 'templates')),
    autoescape=False
)

# Adding api to sys.path
sys.path.extend([os.path.join('alfred', 'modules', 'api')])

user_home_path = os.path.expanduser("~")
user_folder_name = "." + APP_NAME.lower()
user_folder_path = os.path.join(user_home_path, user_folder_name)

# Database
db_name = "alfred.db"

# Classifier
clf_file = "classifier.pkl"

# Modules folder
if(not os.path.isdir(user_folder_path)):
    os.makedirs(user_folder_path)

modules_folder_path = os.path.join(user_folder_path, "modules")
sys.path.extend([modules_folder_path])

if(not os.path.isdir(modules_folder_path)):
    os.makedirs(modules_folder_path)

# Modules server
host_url = 'http://alfredhub.herokuapp.com/'
modules_list_url =  host_url + 'alfred_modules.json'
modules_download_url = host_url + 'alfred_modules/{id}/versions/{version_id}/download'

settings_path = os.path.join(user_folder_path, 'settings.json')
global_settings = Settings(settings_path)
