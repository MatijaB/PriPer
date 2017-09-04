import spotipy

from spotipy.oauth2 import SpotifyClientCredentials

import client


class Spotify(client.Client):
    def __init__(self):
        ccm = SpotifyClientCredentials()
        self.client = spotipy.Spotify(client_credentials_manager=ccm)

    def get_id(self, artist_obj):
        data = self.client.search(type='artist', q=artist_obj.name)

        for artist in sorted(data['artists']['items'], key=lambda k: k['popularity']):
            if artist['name'].lower() == artist_obj.name.lower():
                return artist['id']

        return None

    def get_similar(self, artist_obj):
        if artist_obj.spotify_id is None:
            return None

        data = self.client.artist_related_artists(artist_obj.spotify_id)

        artists = sorted(data['artists'], key=lambda k: k['popularity'])

        return [(artist['name'], artist['id'], artist['popularity']) for artist in artists]

    def get_popularity(self, artist_obj):
        if artist_obj.spotify_id is None:
            return None

        data = self.client.artist(artist_obj.spotify_id)

        if 'popularity' in data:
            return data['popularity']

        return None
