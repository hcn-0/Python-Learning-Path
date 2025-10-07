import requests
import sys
import json

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("http://itunes.apple.com/search?entity=song&limit=10&term=" + sys.argv[1])

songs_name = response.json()

for song in songs_name["results"]:
    print(song["trackName"])
