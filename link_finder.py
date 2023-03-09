#csv into lists
import csv

filename = "track_info.csv"

track_titles = []
track_artists = []
track_duration_ms = []

#adding the data from the csv file into lists to search youtube with
with open(filename, 'r', encoding="utf-8") as csvfile:

    csvreader = csv.reader(csvfile)

    fields = next(csvreader)

    for index, row in enumerate(csvreader):
        if index%2 == 1:
            track_titles.append(row[0])
            track_artists.append(row[1])
            track_duration_ms.append(row[2])

from youtubesearchpython import *

#text file
f = open("links.txt", "w")

#searches yt with above lists and writes link to text file

for count, title in enumerate(track_titles):
    customsearch = CustomSearch(f"{title} {track_artists[count]}", VideoSortOrder.viewCount, limit=1,)
    link1 = customsearch.result()["result"]
    f.write(f"{link1[0]['link']}\n")
    print(f"{link1[0]['title']} added to text file")

print("finished finding links from csv parameters")
f.close()