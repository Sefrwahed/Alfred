import os
import re
import shutil
import zipfile

from alfred import alfred_globals as ag
from alfred.modules.module_info import add_module_info


def install_cached_modules():
    MODULES_CACHE_DIR = os.path.join(ag.user_folder_path, 'cache', 'modules')

    for filename in os.listdir(MODULES_CACHE_DIR):
        file_path = os.path.join(MODULES_CACHE_DIR, filename)
        if zipfile.is_zipfile(file_path):
            install(file_path)


def install(module_zip_path):
    # TODO fetch missing module info
    username = 'Sefrwahed'
    source = 'github.com'

    m = re.fullmatch(r'(?P<name>[\w-]+?)_(?P<version>.+)\.zip',
                     os.path.basename(module_zip_path))
    if m:
        d = m.groupdict()
        name = d['name']
        version = d['version']
    else:
        raise ValueError('Not a valid module file pattern.')

    install_dir = os.path.join(ag.user_folder_path, 'modules',
                               source, username, name)
    tmp_dir = os.path.join(ag.user_folder_path, 'modules',
                           source, username, '.tmp')

    for dir in [install_dir, tmp_dir]:
        if os.path.exists(dir):
            shutil.rmtree(dir)
        os.makedirs(dir)

    module_zip = zipfile.ZipFile(module_zip_path, 'r')
    module_zip.extractall(tmp_dir)  # Extract into .../<usernmae>/.tmp
    module_root_path = os.path.join(tmp_dir, module_zip.namelist()[0])
    module_zip.close()

    # Move .../<usernmae>/.tmp to .../<usernmae>/<name> & clean .tmp directory
    os.rename(module_root_path, install_dir)
    os.removedirs(tmp_dir)

    os.remove(module_zip_path)

    add_module_info(name, source, username, version)
