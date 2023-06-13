from pytube import YouTube
from pytube import Playlist
from sys import argv

while True:
    choice = input("Wanna download video or playlist? (v or p): ")
    if choice == "v":
        link = input("Give video link:")
        yt = YouTube(link)
        yd = yt.streams.get_highest_resolution()
        print(f"You are downloading this beast: {yt.title}, from {yt.author}")
        print(f"Jesus it has: {yt.views} views!")
        yd.download("/Users/user/Desktop/youtube_d/videos")
        break
    elif choice == "p":
        link = input("Give playlist link: ")
        p = Playlist(link)
        print(f"Downloading: {p.title} from {p.owner}")
        print(f"Oof it has: {len(p.videos)} videos!")
        for video in p.videos:
            video.streams.get_highest_resolution().download(
                "/Users/user/Desktop/youtube_d/videos"
            )
        break
    else:
        print("I SAID TYPE v or p !!!\nNOW TRY AGAIN !!!")
