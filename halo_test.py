import spotipy, jsonreader, json
from spotipy.oauth2 import SpotifyClientCredentials
import spotify_feature as sf

client_credentials_manager = SpotifyClientCredentials(client_id=jsonreader.spotify_client_id, client_secret=jsonreader.spotify_client_key)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

halo_tracks = sp.album_tracks('6GSXmRwERX2erR5xuLTajj')

"""
for key in halo_tracks.keys():
	print(key, "\t", halo_tracks[key])
	print("\n\n\n\n")
"""

track_num = len(halo_tracks['items'])
track_uri_list = []

#print(halo_tracks['items'][0].keys())

for _ in range(track_num):
	track_uri_list.append(halo_tracks['items'][_]['uri'].split(':')[-1])

sf.dumpFeatures(track_uri_list)

#print(sf.dumpFeatures())
