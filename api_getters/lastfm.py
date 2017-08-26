import json
import requests

import client


class LastFm(client.Client):
    APIKEY = "0d2dcafbf96aafcea7b77c7a54d2552e"
    SECRET = "b13876c1031e15fc8123d6d58e98e33d"

    ENDPOINT = "http://ws.audioscrobbler.com/2.0/"

    def get_similar(self, artist_obj):
        params = {
            'format': 'json',
            'method': 'artist.getsimilar',
            'api_key': self.APIKEY
        }

        if artist_obj.mbid is None:
            params['artist'] = artist_obj.formatted_name
        else:
            params['mbid'] = artist_obj.mbid

        response = requests.get(self.ENDPOINT, params=params)
        data = json.loads(response.text)

        if 'similarartists' not in data and params['mbid'] is not None:
            params['mbid'] = None
            params['artist'] = artist_obj.formatted_name

            response = requests.get(self.ENDPOINT, params=params)
            data = json.loads(response.text)

        if 'similarartists' not in data:
            return None

        return [v['name'] for v in data['similarartists']['artist']]
