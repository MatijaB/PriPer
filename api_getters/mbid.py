# http://musicbrainz.org/ws/2/artist/?query=artist:growlers&fmt=json

# todo get mbid of artist from here
import sys
import json
import urllib

URL = "http://musicbrainz.org/ws/2/artist/?query=artist:{formatted_name}&fmt=json"


def get_mbid(artist_name):
    formatted_name = artist_name.lower().replace("the", "").strip().replace(" ", "%20")

    print formatted_name

    response = urllib.urlopen(URL.format(formatted_name=formatted_name))

    data = json.loads(response.read())

    for artist in data['artists']:
        if artist_name in (artist['name'], artist['sort-name']):
            print artist
            return artist['id']

if __name__ == '__main__':
    print get_mbid(sys.argv[1])
