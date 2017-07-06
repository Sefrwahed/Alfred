import os
import shutil
import zipfile

# Qt imports
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot

# Local imports
from alfred import alfred_globals as ag
# from alfred.nlp.classifier import Classifier
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

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls()

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

        from alfred.nlp import Classifier
        Classifier().train()
        self.installation_finished.emit(int(self.module_data['id']))

    @pyqtSlot(int)
    def uninstall(self, mod_id):
        info = ModuleInfo.find_by_id(mod_id)
        print(mod_id)
        print('{m}'.format(m=info))
        Logger().info("Uninstalling module {} v{}".format(
            info.name, info.version
        ))
        module_folder_path = os.path.join(ag.modules_folder_path,
                                          info.source, info.user, info.name)

        try:
            shutil.rmtree(module_folder_path)
        except Exception as ex:
            Logger().err(ex)

        info.destroy()
        self.uninstallation_finished.emit(info.id)
        Logger().info("Unistalled module successfully")
        from alfred.nlp import Classifier
        Classifier().train()

    @pyqtSlot(dict)
    def update(self, mod_data):
        self.uninstall(mod_data["id"])
        self.download(mod_data)
