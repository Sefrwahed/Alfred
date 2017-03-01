import os
import zipfile

import pip

from alfred import alfred_globals as ag
from alfred.modules.module_info import add_module_info
from alfred.nlp import classifier


def install_cached_modules():
    MODULES_CACHE_DIR = os.path.join(ag.user_folder_path, 'cache', 'modules')

    for filename in os.listdir(MODULES_CACHE_DIR):
        file_path = os.path.join(MODULES_CACHE_DIR, filename)
        if zipfile.is_zipfile(file_path):
            install(file_path)


def install(mod_data, module_zip_path):
    name = mod_data['name']
    version = mod_data['latest_version']['number']
    username = 'Sefrwahed'
    source = 'github.com'

    path = f'git+git://github.com/n1amr/{mod_data["name"]}.git@master'
    pip.main(['install', path])
    # TODO add installation path to module_info in database
    add_module_info(name, source, username, version)

    classifier.train()
