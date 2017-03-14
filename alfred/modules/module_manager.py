import os
import shutil
import zipfile

# Qt imports
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot

# Local imports
from alfred import alfred_globals as ag
from alfred.nlp import Classifier
from . import RequestThread
from .module_info import ModuleInfo
from alfred.logger import Logger


class ModuleManager(QObject):
    _instance = None

    data_fetched = pyqtSignal(list)
    conn_err = pyqtSignal()
    installation_finished = pyqtSignal(int)
    uninstallation_finished = pyqtSignal(int)
    update_finished = pyqtSignal(int)

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
            self.install()

    @pyqtSlot(dict)
    def download(self, module):
        Logger().info(
            "Downloading {} v{}".format(
                module["name"], module["latest_version"]["number"]
            )
        )
        self.create_thread()
        self.rthread.purpose = "download"
        self.mod_data = module
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

    def install(self):
        # TODO fetch missing module info
        source = 'alfredhub'

        name = self.mod_data['name']
        username = self.mod_data['user']['username']
        version = self.mod_data['latest_version']['number']

        install_dir = os.path.join(ag.user_folder_path, 'modules',
                                   source, username, name)

        Logger().info("Installing module {}".format(name))
        Logger().info("Installation dir is {}".format(install_dir))
        for dir in [install_dir]:
            if os.path.exists(dir):
                shutil.rmtree(dir)
            os.makedirs(dir)

        module_zip = zipfile.ZipFile(self.module_zip_path, 'r')
        module_zip.extractall(install_dir)
        module_zip.close()

        os.remove(self.module_zip_path)

        info = ModuleInfo(name, source, username, version)
        info.create()
        Classifier().train()
        self.installation_finished.emit(int(self.mod_data['id']))

    def uninstall(self, mod_id):
        info = ModuleInfo.find_by_id(mod_id)
        Logger().info("Uninstalling module {} v{}".format(
            info.name, info.version
        ))
        module_folder_path = os.path.join(ag.modules_folder_path,
                                          info.source, info.user, info.name)

        try:
            shutil.rmtree(module_folder_path)
        except Exception as ex:
            print(ex)

        info.destroy()
        self.uninstallation_finished.emit(mod_id)
        Logger().info("Unistalled module successfully")
        Classifier().train()

    def update(self, mod_data):
        self.uninstall(mod_data)
        self.install(mod_data)