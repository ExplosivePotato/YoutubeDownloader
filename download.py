import youtube_dl
import argparse
import sys
import os


DEFAULT_DOWNLOAD_PATH = os.environ['USERPROFILE'] + r"\Downloads"
YDL_DEFAULT_OPTIONS = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',}],}


def download_videos(args):
    download_options = get_options(args)

    os.chdir(args.path)
    with youtube_dl.YoutubeDL(download_options) as ydl:
        for url in args.urls:
            print "Downloading: " + url
            ydl.download([url])
            print "\n"


def get_options(args):
    download_options = {}
    if not args.video:
        download_options = dict(YDL_DEFAULT_OPTIONS)
    return download_options


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", '--url', help="The url to download", action='append', dest='urls')
    parser.add_argument("-p", help="The path the file will be saved to", action='store', dest='path', default=DEFAULT_DOWNLOAD_PATH)
    parser.add_argument("--video", help="Used to download as a video, Default is only audio", action='store_true')
    args = parser.parse_args()
    sys.exit(download_videos(args))