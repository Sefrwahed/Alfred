from jinja2 import Environment, FileSystemLoader
import os
import sys

APP_NAME = "Alfred"
WIT_TOKEN = "GMCAOZ4HFZ3Q5K7FNOFIQSR6VCM6NA47"

main_components_env = Environment(
    loader=FileSystemLoader(os.path.join('alfred', 'modules', 'templates')),
    autoescape=False
)

# Adding api to sys.path
sys.path.extend([os.path.join('alfred', 'modules', 'api')])

# Modules folder
user_home_path = os.path.expanduser("~")
user_folder_name = "." + APP_NAME.lower()
user_folder_path = os.path.join(user_home_path, user_folder_name)

if(not os.path.isdir(user_folder_path)):
    os.makedirs(user_folder_path)


modules_folder_path = os.path.join(user_folder_path, "modules")
sys.path.extend([modules_folder_path])

if(not os.path.isdir(modules_folder_path)):
    os.makedirs(modules_folder_path)
