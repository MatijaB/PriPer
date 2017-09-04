import os
import sys

from api_getters import Artist

os.system('. config/production.sh')

if __name__ == '__main__':
    test_artist = Artist(sys.argv[1])

    print test_artist.formatted_name
    print test_artist.mbid
    print test_artist.popularity
    sa = test_artist.similar_artists

    for artist_obj in sa.values():
        print artist_obj.name, artist_obj.popularity
