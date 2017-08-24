import json
import urllib

class Artist(object):
    MUSIC_BRAINZ_URL = "http://musicbrainz.org/ws/2/artist/?query=artist:{formatted_name}&fmt=json"

    def __init__(self, name):
        self.name = name
        self._mbid = None

    @property
    def mbid(self):

        if self._mbid is None:

            formatted_name = urllib.quote(self.name.lower().replace("the", "").strip())

            response = urllib.urlopen(self.MUSIC_BRAINZ_URL.format(formatted_name=formatted_name))

            data = json.loads(response.read())

            for artist in data['artists']:
                if self.name.lower() in (artist['name'].lower(), artist['sort-name'].lower()):
                    self._mbid = artist['id']

        return self._mbid


class Client(object):

    def __init__(self):
        pass

    def get_similarity(self, artist_name, artist_mbid):
        raise NotImplementedError

    def get_popularity(self, artist_name, artist_mbid):
        raise NotImplementedError

    def get_mbid(self, artist_name):
        raise NotImplementedError

