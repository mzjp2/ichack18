import json

# usage
# import jsonreader.py
# jsonreader.spotify_client_id  will be the string for your client id
#  



with open('api_keys.json', 'r') as f:
	data = json.load(f)


spotify_client_id = data['spotify']['client_id']
spotify_client_key = data['spotify']['client_key']

mscv_key =  data['microsoft']['api_key']