import os
import json
import requests

import client


class LastFm(client.Client):
    APIKEY = os.environ.get("LASTFM_APIKEY", "")
    SECRET = os.environ.get("LASTFM_SECRET", "")

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
