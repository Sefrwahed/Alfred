import os
import shutil
import zipfile

from alfred import alfred_globals as ag
from alfred.modules.module_info import add_module_info
from alfred.modules.module_info import delete_module_info
from alfred.nlp import classifier


def install_cached_modules():
    MODULES_CACHE_DIR = os.path.join(ag.user_folder_path, 'cache', 'modules')

    for filename in os.listdir(MODULES_CACHE_DIR):
        file_path = os.path.join(MODULES_CACHE_DIR, filename)
        if zipfile.is_zipfile(file_path):
            install(file_path)


def install(mod_data, module_zip_path):
    # TODO fetch missing module info
    username = 'Sefrwahed'
    source = 'github.com'

    name = mod_data['name']
    version = mod_data['latest_version']['number']

    install_dir = os.path.join(ag.user_folder_path, 'modules',
                               source, username, name)
    # tmp_dir = os.path.join(ag.user_folder_path, 'modules',
                           # source, username, '.tmp')

    for dir in [install_dir]:
        if os.path.exists(dir):
            print("rem")
            shutil.rmtree(dir)
        os.makedirs(dir)

    module_zip = zipfile.ZipFile(module_zip_path, 'r')
    module_zip.extractall(install_dir)
    module_zip.close()

    # Move .../<usernmae>/.tmp to .../<usernmae>/<name> & clean .tmp directory
    # os.rename(module_root_path, install_dir)
    # os.removedirs(tmp_dir)

    os.remove(module_zip_path)

    add_module_info(name, source, username, version)
    classifier.train()


def uninstall(mod_data):

    username = 'Sefrwahed'
    source = 'github.com'
    name = mod_data['name']

    module_folder_path = os.path.join(ag.modules_folder_path,
                                      source, username, name)

    try:
        shutil.rmtree(module_folder_path)
    except Exception as ex:
        print(ex)

    delete_module_info(mod_data["id"])
    classifier.train()


def update(mod_data):
    uninstall(mod_data)
    install(mod_data)
    pass
