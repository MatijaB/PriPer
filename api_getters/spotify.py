import json
import requests

import client


class Spotify(client.Client):
    ENDPOINT = ""

    def __init__(self):
        #todo initialize authorization
        pass

    def refresh_authorization(self):
        #todo refresh authorization if needed
        pass

    def get_similar(self, artist_obj):
        params = {
        }
        return None

    def get_popularity(self, artist_obj):
        pass