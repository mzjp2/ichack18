import spotipy
import jsonreader
import sys
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util

scope = 'playlist-modify-private'
username = 'cl1zn6lqeumrukzr0il0j2j24'

token = util.prompt_for_user_token(username, scope, 
									client_id=jsonreader.spotify_client_id,
									client_secret=jsonreader.spotify_client_key, 
									redirect_uri='http://localhost/')

if token:
	sp = spotipy.Spotify(auth = token)
	sp.trace = False
	playlists = sp.user_playlist_create(username, 'background', public=False)
else:
	print("Can't get token")