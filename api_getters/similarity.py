import json
import urllib


class LastFm():
    APIKEY = "0d2dcafbf96aafcea7b77c7a54d2552e"
    SECRET = "b13876c1031e15fc8123d6d58e98e33d"

    url_endpoint = "http://ws.audioscrobbler.com/2.0/" \
                   "?method=artist.getsimilar&artist={ARTIST}&api_key={APIKEY}&format=json"

    def _get_similar(self, artist):
        response = urllib.urlopen(self.url_endpoint.format(ARTIST=artist, APIKEY=self.APIKEY))
        data = json.loads(response.read())

        return data

    def get_similar(self, artist):
        data = self._get_similar(artist)

        if 'similarartists' not in data:
            return None

        artist_list = [v['name'] for v in data['similarartists']['artist']]
        return artist_list