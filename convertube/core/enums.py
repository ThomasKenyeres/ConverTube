import os

class VideoFormat:
    MP4 = "mp4"
    WEBM = "webm"
    MKV = "mkv"

class AudioFormat:
    MP3 = "mp3"

class CT_ENV:
    default_download_path = "CT_DEFAULT_DL_PATH"

class CT_Conf:
    base_path = str(os.getenv("HOME")) + "/.local/share/convertube"
    conf_file = base_path + "/conf.json"
    video_cache_path = base_path + "/video_cache"
    initial_dl_path = str(os.getenv("HOME")) + "/ConverTubeDownloads"