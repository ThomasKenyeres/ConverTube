import os

from convertube.core import cli_helper
from convertube.core.enums import VideoFormat


def yt_url_is_valid(url):
    #TODO: implement validation
    return True

def download_video(url, dl_path, video_format=VideoFormat.MP4):
    os.chdir(dl_path)
    video_title_cmd = ["youtube-dl", "--get-filename", "-o", "%(title)s", str(url)]
    video_name_cmd = ["youtube-dl", "--get-filename", "-o", "%(title)s.%(ext)s", str(url)]
    video_ext_cmd = ["youtube-dl", "--get-filename", "-o", "%(ext)s", str(url)]

    video_title = str(cli_helper.run_command(video_title_cmd)).strip()
    video_name = str(cli_helper.run_command(video_name_cmd)).strip()
    video_ext = str(cli_helper.run_command(video_ext_cmd)).strip()
    filename = str(video_title) + "." + str(video_format)
    print(str(video_title) + " " + str(video_format) + " >>> >>> " + str(filename))

    # TODO: use youtube-dl python library
    cmd = ["youtube-dl", "-f", str(video_format), "-o", str(video_title) + "." + str(video_format), str(url)]

    out = str(cli_helper.run_command(cmd))

    return {
        "title": video_title,
        "name": video_name,
        "path": dl_path,
        "requested_format": video_format,
        "filename": filename
    }

def convert_video_to_mp3(video_path, new_mp3_path):
    pass

def empty_video_cache():
    pass

