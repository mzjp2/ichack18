import json



with open('api_keys.json', 'r') as f:
	#json.dump(data, f)
	data = json.load(f)

print(data['spotify'])

spotify_client_id = data['spotify']['client_id']
spotify_client_key = data['spotify']['client_key']

mscv_key =  