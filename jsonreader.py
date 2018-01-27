import json

"""
api_keys_txt = open('api_keys.txt', 'r')
json.load(api_keys_txt)
"""

#data = {"spotify": {"client_id": "583a83fba9c643948baba0fca6d9a605", "client_key": "e44f01d107264e17aa2daad773dc1314"}, "microsoft":{"api_key": ""}}


with open('api_keys.json', 'r') as f:
	#json.dump(data, f)
	data = json.load(f)

print(data)