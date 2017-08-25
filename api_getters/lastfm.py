import json
import requests

import client


class LastFm(client.Client):
    APIKEY = "0d2dcafbf96aafcea7b77c7a54d2552e"
    SECRET = "b13876c1031e15fc8123d6d58e98e33d"

    ENDPOINT = "http://ws.audioscrobbler.com/2.0/?method=artist.getsimilar"

    def get_similar(self, artist):
        assert isinstance(artist, client.Artist), "wrong object type"

        params = {
            'format': 'json',
            'api_key': self.APIKEY
        }

        if artist.mbid is None:
            params['artist'] = artist.formatted_name
        else:
            params['mbid'] = artist.mbid

        response = requests.get(self.ENDPOINT, params=params)

        data = json.loads(response.text)

        if 'similarartists' not in data:
            return None

        similar_artists = [v['name'] for v in data['similarartists']['artist']]

        return similar_artists
