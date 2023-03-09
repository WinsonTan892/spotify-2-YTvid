#from text files into downloaded videos
from pytube import YouTube

#youtube folder on desktop
save_path = r"C:\Users\winso\Desktop\youtube"

link = open("links.txt","r")

#downloads from the links in the txt file
for i in link:
    try:
        yt = YouTube(i)
        mp4files = yt.streams.filter(only_audio=True, file_extension="mp4").order_by("abr").desc().first().download(save_path)
        print(f"'{yt.title}' Download Completed")

    except Exception as e:
        print(f"Error: {e}")

print("finished downloading")