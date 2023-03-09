#from spotify link into csv
import csv
import os
import re

import spotipy
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyClientCredentials

#credentials from env file
load_dotenv()
client_id = os.getenv("client_id", "")
client_secret = os.getenv("client_secret", "")
output_file_name = "track_info.csv"

#user inputs their playlist they want to download
PLAYLIST_LINK = input("Input Spotify playlist link:")

#authenticates my credentials from aforementioned env file
client_credentials_manager = SpotifyClientCredentials(client_id=client_id,client_secret=client_secret)

#spotify session object is created
session = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

#Spotify URI is extracted from the link user inputs, raises error if wrong format
if match := re.match(r"https://open.spotify.com/playlist/(.*)\?",PLAYLIST_LINK):
    playlist_uri = match.groups()[0]
else:
    raise ValueError("Expected format: https://open.spotify.com/playlist/...")

#list of tracks generated from playlist
tracks = session.playlist_tracks(playlist_uri)["items"]

#writing to the csv file 
with open(output_file_name,"w",encoding="utf-8") as file:
    writer = csv.writer(file)

    #more parameters can be added here (there's stuff like danceability and valence???)
    writer.writerow(["track", "artist", "length"])

    for track in tracks:
        name = track["track"]["name"]
        artists = ", ".join(
            [artist["name"] for artist in track["track"]["artists"]]
        )
        length = track["track"]["duration_ms"]

        writer.writerow([name, artists, length])
        print(f"{name} by {artists} added to csv")

print("finished converting playlist into csv file")