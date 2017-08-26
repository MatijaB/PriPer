import json
import requests

import client


class MusicBrainz(client.Client):
    ENDPOINT = "http://musicbrainz.org/ws/2/artist/"
    QUERY = "artist:{formatted_name}"

    def get_mbid(self, artist_obj):
        query = self.QUERY.format(formatted_name=artist_obj.formatted_name)
        params = {
            'fmt': 'json',
            'query': query
        }

        response = requests.get(self.ENDPOINT, params=params)

        data = json.loads(response.text)

        for artist_json in data['artists']:
            if artist_obj.name.lower() in (artist_json['name'].lower(), artist_json['sort-name'].lower()):
                return artist_json['id']

        return None
