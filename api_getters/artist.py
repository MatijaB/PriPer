import urllib

from lastfm import LastFm
from musicbrainz import MusicBrainz
from spotify import Spotify


class SimilarArtistsList(dict):

    def __setitem__(self, key, value):
        if not isinstance(value, Artist):
            raise TypeError, "item is not an instance of the Artist class"

        if key in self.keys():
            self[key].update(value)
            return

        super(SimilarArtistsList, self).__setitem__(key, value)


class Artist(object):
    _eventbrite = None
    _lastfm = None
    _musicbrainz = None
    _spotify = None
    _mbid = None
    _spotify_id = None
    _popularity = None

    _similar_artists = SimilarArtistsList()

    def __init__(self, name, **kwargs):
        self.name = name

        for key, value in kwargs.items():
            if key in dir(self):
                self.__dict__[key] = value

    def update(self, other):
        for key, value in other.__dict__.iteritems():
            if self.__getattribute__(key) is None:
                self.__setattr__(key, value)

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
    def spotify(self):
        if self._spotify is None:
            self._spotify = Spotify()

        return self._spotify
    
    @property
    def mbid(self):
        if self._mbid is None:
            self._mbid = self.musicbrainz.get_mbid(self)

        return self._mbid

    @property
    def similar_artists(self):
        if not self._similar_artists:
            self._similar_artists_lastfm()
            self._similar_artists_spotify()

        return self._similar_artists

    def _similar_artists_lastfm(self):
        lastfm_similar_artists = self.lastfm.get_similar(self)

        for name in lastfm_similar_artists:
            similar_artist_obj = Artist(name)
            self._similar_artists[similar_artist_obj.formatted_name] = similar_artist_obj

    def _similar_artists_spotify(self):
        spotify_similar_artists = self.spotify.get_similar(self)

        for name, spotify_id, popularity in spotify_similar_artists:
            similar_artist_obj = Artist(name, _spotify_id=spotify_id, _popularity=popularity)
            self._similar_artists[similar_artist_obj.formatted_name] = similar_artist_obj

    @property
    def spotify_id(self):
        if self._spotify_id is None:
            self._spotify_id = self.spotify.get_id(self)

        return self._spotify_id

    @property
    def popularity(self):
        if self._popularity is None:
            self._popularity = self.spotify.get_popularity(self)

        return self._popularity
