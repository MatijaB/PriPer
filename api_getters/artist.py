import urllib

from lastfm import LastFm
from musicbrainz import MusicBrainz


class Artist(object):

    def __init__(self, name):
        self.name = name

        self._eventbrite = None
        self._lastfm = None
        self._musicbrainz = None
        self._spotify = None

        self._mbid = None
        self._similar_artists = None

    @property
    def formatted_name(self):
        return urllib.quote(self.name.lower().replace("the", "").strip())

    @property
    def musicbrainz(self):
        if self._musicbrainz is None:
            self._musicbrainz = MusicBrainz()

        return self._musicbrainz

    @property
    def lastfm(self):
        if self._lastfm is None:
            self._lastfm = LastFm()

        return self._lastfm

    @property
    def mbid(self):
        if self._mbid is None:
            self._mbid = self.musicbrainz.get_mbid(self)

        return self._mbid

    @property
    def similar_artists(self):
        if self._similar_artists is None:
            self._similar_artists = self.lastfm.get_similar(self)

        return self._similar_artists
