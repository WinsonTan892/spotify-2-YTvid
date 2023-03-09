# spotify-2-YTvid
Python script that gets users spotify playlist and downloads matching/similar videos from youtube

Used spotipy, youtube-search-python and pytube libraries.

https://spotipy.readthedocs.io/en/2.22.1/

https://pytube.io/en/latest/

https://pypi.org/project/youtube-search-python/

The script basically gets playlist info from the spotify web api, turns the info into a csv file, uses the parameters in the csv file(name, artist, length) to search for corresponding youtube video (sorted by viewcount), gets the link and proceeds to download it.

I had a bunch of unicode and encoding errors cause half of my playlist was jpop and the titles were in japanese, so working through that was kind of a pain. I wasn't using github at the time so yeah that's why theres only one version.

This is one of my first projects that I didn't just regurgitate from a tutorial. Although, I did reference a lot of other guides, videos and instructionals on different aspects of the script, so if you see familiar code thats probably why (I will try to list them if i remember). And also reading the documentation.

If you want to use the script (I would not recommend it, it doesn't get the right vid 100% of the time) you should make a folder called "youtube" on your desktop cause thats what I set the file directory to download as. And also you have to set up the spotipy authorization stuff in a .env file.

As for the legal ramifications of this, I don't really know. Just don't redistribute whatever you downloaded for monetary gain or claim that it is your own I guess? This is just a personal project, please don't sue me.
