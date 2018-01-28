import spotipy, jsonreader, json, sys
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util

scope = 'playlist-read-private playlist-modify-private playlist-read-collaborative'
username = 'cl1zn6lqeumrukzr0il0j2j24'

token = util.prompt_for_user_token(username, scope, 
									client_id=jsonreader.spotify_client_id,
									client_secret=jsonreader.spotify_client_key, 
									redirect_uri='http://localhost/')

if token:
	sp = spotipy.Spotify(auth = token)
	sp.trace = False
else:
	print("Can't get token")

def playlistCreate():
	playlists = sp.user_playlist_create(username, 'Background Music', public=False)
	results = sp.current_user_playlists()
	for i, item in enumerate(results['items']):
		if "{name}".format(name = item['name']) == 'Background Music':
			created_playlist_id = "{id}".format(id=item['id'])
	return created_playlist_id

def playlistAdd(created_playlist_id, tracks_list):
	user_playlist_add_tracks(username, created_playlist_id, tracks_list)
	return None

	
