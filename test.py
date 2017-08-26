import sys

from api_getters import Artist


if __name__ == '__main__':
    test_artist = Artist(sys.argv[1])

    print test_artist.formatted_name
    print test_artist.mbid
    print test_artist.similar_artists