from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)

print("Title: ", yt.title)
print("Channel: ", yt.author)
print("Views: ", yt.views)

yd = yt.streams.get_audio_only()
yd.download('/mnt/d/YT_Downloads/Audios')