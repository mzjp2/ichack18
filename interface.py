import time
from playlist import *
from tkinter.filedialog import askopenfilename
import tkinter as tk
import spotipy, jsonreader, json, sys, os, webbrowser
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
import numpy as np
from tagtospot import tag_to_mood
from analyse_image import get_image_tags
from spotify_feature import generateGenre
from spotify_feature import recommendedList


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self, height = 10, width = 25)
        self.hi_there["text"] = "Team SSA Image to Playlist"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")
        self.hi_there["font"] = ("Helvetica", 16)

        self.quit = tk.Button(self, text="Upload Image", fg="red",
                              command=root.destroy, height = 10, width = 25, font = ("Helvetica", 16))
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("Made by Christopher Smith, Joe Rosenberg, Khalid Hassan and Zain Patel")

root = tk.Tk()
root.geometry("1000x1000")
app = Application(master=root)
app.mainloop()
filename = askopenfilename()

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
	results = sp.current_user_playlists()
	for i, item in enumerate(results['items']):
		if "{name}".format(name = item['name']) == 'Background Music':
			old_playlist_id = "{id}".format(id=item['id'])
			sp.user_playlist_unfollow(username, old_playlist_id)

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
	image = filename
	curr_img_tags = get_image_tags(image)
	spot_tags = tag_to_mood(curr_img_tags)
	genre_list = generateGenre(spot_tags)
	track_list = recommendedList(genre_list, 5)
	print(genre_list)
	id = playlistCreate()
	playlistAdd(id, track_list)
	webbrowser.open('https://open.spotify.com/user/' + username + '/playlist/' + id)