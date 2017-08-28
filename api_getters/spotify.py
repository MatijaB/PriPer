import os
import json
import spotipy

from spotipy.oauth2 import SpotifyClientCredentials

import client


class Spotify(client.Client):
    def __init__(self):
        ccm = SpotifyClientCredentials()
        self.client = spotipy.Spotify(client_credentials_manager=ccm)

    def refresh_authorization(self):
        #todo refresh authorization if needed
        pass

    def get_similar(self, artist_obj):
        params = {
        }
        return None

    def get_popularity(self, artist_obj):
        data = self.client.search(type='artist', q=artist_obj.name)

        for artist in data['artists']['items']:
            if artist['name'].lower() == artist_obj.name.lower():
                return artist['popularity']

        return None