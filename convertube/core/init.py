import os
import os.path as IO
from convertube.core.enums import CT_Conf, CT_ENV

def dir_exists(path):
    if IO.exists(path):
        if IO.isdir(path):
            return True
    return False

def file_exists_not_dir(path):
    if IO.exists(path):
        return not IO.isdir(path)
    return False


def base_exists():
    return IO.exists(CT_Conf.base_path)

def all_files_exist():
    return base_exists() \
           and file_exists_not_dir(CT_Conf.conf_file) \
           and dir_exists(CT_Conf.video_cache_path)

def create_base():
    os.makedirs(CT_Conf.base_path)

def create_video_cache():
    os.makedirs(CT_Conf.video_cache_path)

def create_conf_file():
    with open(CT_Conf.conf_file, "w+") as conf_file:
        conf_file.write("text")

def create_dl_directory():
    os.makedirs()

def create_all():
    os.makedirs(CT_Conf.video_cache_path)
    create_conf_file()

def set_dlpath_env(path):
    #os.environ[CT_ENV.default_download_path] = str(path)
    dl_path = CT_ENV.default_download_path
    cmd = "export " + dl_path + "=\"" + path.replace("\"", "\\\"") + "\""
    print(cmd)
    os.system(cmd)

def init():
    dl_path = os.getenv(CT_ENV.default_download_path)
    if dl_path is "" or dl_path is None:
        set_dlpath_env(CT_Conf.initial_dl_path)
        print(os.getenv(CT_ENV.default_download_path))
    if not all_files_exist():
        if not base_exists():
            create_all()
        else:
            if not dir_exists(CT_Conf.video_cache_path):
                create_video_cache()
            if not file_exists_not_dir(CT_Conf.conf_file):
                create_conf_file()
