import os
import alfred.alfred_globals as ag


def global_file_path(global_file):
    return os.path.join(ag.user_folder_path, global_file)
