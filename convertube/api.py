import shutil

from convertube.core.calls import yt_url_is_valid, download_video, convert_video_to_mp3
from convertube.core.enums import VideoFormat, AudioFormat, CT_Conf


def download_and_convert(url, mp3_target_path,
                         mp3_filename=None,
                         video_format=VideoFormat.MP4, audio_format=AudioFormat.MP3,
                         keep_video=False, video_path=None):
    if yt_url_is_valid(url):
        video_datas = download_video(url, CT_Conf.video_cache_path, video_format=video_format)
        video_cpath = CT_Conf.video_cache_path + "/" + video_datas["filename"]
        if keep_video is not None and video_path is not None:
            video_name = video_datas["filename"]
            shutil.copy(video_cpath, video_path)
        if audio_format is AudioFormat.MP3:
            if mp3_filename is not None:
                new_mp3_path = video_datas["path"] + "/" + video_datas["title"] + ".mp3"
            mp3_cpath = mp3_target_path + "/" + video_datas["title"] + ".mp3"
            convert_video_to_mp3(video_cpath, mp3_cpath)
    else:
        print("invalid url")

def collect_videos(urls, video_format=VideoFormat.MP4, video_path=None):
    pass

def convert_all_in_cache_to_mp3(path):
    pass