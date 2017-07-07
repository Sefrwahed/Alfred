import os, shutil, zipfile, random

# Qt imports
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot

# Local imports
from alfred import alfred_globals as ag
from . import RequestThread
from .module_info import ModuleInfo
from alfred.logger import Logger

import tarfile


class ModuleManager(QObject):
    _instance = None

    module_data = None
    data_fetched = pyqtSignal(list)
    conn_err = pyqtSignal()
    installation_finished = pyqtSignal(int)
    uninstallation_finished = pyqtSignal(int)
    signal_train = pyqtSignal()
    update_flag = False
    modules_count = len(ModuleInfo.all())

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls()
            cls._instance.update_flag = False

        return cls._instance

    def create_thread(self):
        if not hasattr(self, 'rthread'):
            self.rthread = RequestThread()
            Logger().info("Created request thread")
            self.rthread.signal_finished.connect(self.thread_finished)
            Logger().info("Connected request thread")

    @pyqtSlot()
    def thread_finished(self):
        if self.rthread.conn_err:
            self.conn_err.emit()
            return

        if self.rthread.purpose == "list":
            self.data_fetched.emit(self.rthread.data)
        else:
            self.install(self.module_data)

    @pyqtSlot(dict)
    def download(self, module):
        Logger().info(
            "Downloading {} v{}".format(
                module["name"], module["latest_version"]["number"]
            )
        )
        self.create_thread()
        self.rthread.purpose = "download"
        self.module_data = module
        self.rthread.url = ag.modules_download_url.format(
            id=module["id"],
            version_id=module["latest_version"]["id"]
        )
        self.module_zip_path = self.rthread.zip_path = os.path.join(
            ag.user_folder_path, module["name"]
        )
        self.rthread.start()

    @pyqtSlot()
    def fetch_data(self):
        self.create_thread()
        self.rthread.purpose = "list"
        self.rthread.start()

    @pyqtSlot(dict)
    def install(self, mod_data):
        # TODO fetch missing module info
        source = 'alfredhub'

        mod_id = mod_data['id']
        name = mod_data['name']
        username = mod_data['user']['username']
        version = mod_data['latest_version']['number']

        install_dir = os.path.join(ag.user_folder_path, 'modules',
                                   source, username, name)

        Logger().info("Installing module {}".format(name))
        Logger().info("Installation dir is {}".format(install_dir))
        for directory in [install_dir]:
            if os.path.exists(directory):
                shutil.rmtree(directory)
            os.makedirs(directory)

        path = self.module_zip_path

        if zipfile.is_zipfile(path):
            module_file = zipfile.ZipFile(path, 'r')
        elif tarfile.is_tarfile(path):
            module_file = tarfile.open(path)
        else:
            msg = '{path} is not a valid zip or tar file'.foramt(path=path)
            Logger().err(msg)
            raise IOError(msg)

        module_file.extractall(install_dir)
        module_file.close()

        os.remove(self.module_zip_path)
        info = ModuleInfo(mod_id, name, source, username, version)
        info.create()

        if self.update_flag:
            shutil.copytree(self.data_backup_path, os.path.join(info.root(), "data"))
            shutil.rmtree(self.data_backup_path)
            self.update_flag = False
        else:
            shutil.copytree(
                os.path.join(os.path.dirname(__file__), "default_data_folder"), 
                os.path.join(install_dir, "data")
            )
        
        self.installation_finished.emit(int(self.module_data['id']))
        self.modules_count += 1
        self.signal_train.emit()

    @pyqtSlot(int)
    def uninstall(self, mod_id, retrain=True):
        info = ModuleInfo.find_by_id(mod_id)
        Logger().info("Uninstalling module {} v{}".format(
            info.name, info.version
        ))
        module_folder_path = info.root()

        try:
            shutil.rmtree(module_folder_path)
        except Exception as ex:
            Logger().err(ex)

        info.destroy()
        self.uninstallation_finished.emit(info.id)
        Logger().info("Unistalled module successfully")
        self.modules_count -= 1
        if retrain:
            self.signal_train.emit()

    @pyqtSlot(dict)
    def update(self, mod_data):
        # backing up data folder
        try:
            info = ModuleInfo.find_by_id(mod_data["id"])
            random_folder_name = "tmp_{}".format(random.randint(1, 1000000000000))
            self.data_backup_path = os.path.join(ag.tmp_folder_path, random_folder_name)
            data_path = os.path.join(info.root(), "data")
            shutil.copytree(data_path, self.data_backup_path)
            
            # updating
            self.update_flag = True
            self.uninstall(mod_data["id"], False)
            self.download(mod_data)

        except Exception as ex:
            Logger().err(ex)
