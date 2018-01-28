import spotipy, jsonreader, json, sys, os, webbrowser
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
import numpy as np
from tagtospot import tag_to_mood
from analyse_image import get_image_tags
from spotify_feature import generateGenre
from spotify_feature import recommendedList

scope = 'playlist-read-private playlist-modify-private playlist-read-collaborative'
username = 'zain.patel6'

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
	sp.user_playlist_add_tracks(username, created_playlist_id, tracks_list)
	return None

if __name__ == '__main__':
	image = 'room.jpg'
	curr_img_tags = get_image_tags(image)
	spot_tags = tag_to_mood(curr_img_tags)
	genre = generateGenre(spot_tags)
	print(genre)
	track_list = recommendedList(genre, 5)
	id = playlistCreate()
	playlistAdd(id, track_list)
	webbrowser.open('https://open.spotify.com/user/' + username + '/playlist/' + id)


