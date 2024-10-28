from pytube import YouTube
from pathlib import Path
from os import *
from pywebio.input import * 
from pywebio.output import *

def video_download():
    while True:
        video_link = input("Enter the YouTube video URL: ") 
        if video_link.startswith("https://"):
            put_text("Downloading...").style('color: red; font-size: 50px')
            video_url = YouTube(video_link) 
            video = video_url.streams.get_highest_resolution()
            path_to_download = "/home/viizinho/Downloads"
            video.download(path_to_download)
            put_text("Download completed successfully!").style('color: red; font-size: 50px')

if __name__ == "__main__":
    video_download()