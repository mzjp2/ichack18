########### Python 3.6 #############
import requests, base64, os, json

headers = {
    # Request headers.
    'Content-Type': 'application/octet-stream',

    # NOTE: Replace the "Ocp-Apim-Subscription-Key" value with a valid subscription key.
    'Ocp-Apim-Subscription-Key': '277f2ecc5dba4d29892eb89537126bb6',
}

params = {
    # Request parameters. All of them are optional.
    'visualFeatures': 'tags',
    'language': 'en',
}

# Replace the three dots below with the full file path to a JPEG image of a celebrity on your computer or network.
image = open('C:/Users/Zain/Documents/Python/hello-world/chatpps/queens_perform.jpg','rb').read() # Read image file in binary mode

# try:
#     # NOTE: You must use the same location in your REST call as you used to obtain your subscription keys.
#     #   For example, if you obtained your subscription keys from westus, replace "westcentralus" in the 
#     #   URL below with "westus".
#     response = requests.post(url = 'https://westeurope.api.cognitive.microsoft.com/vision/v1.0/analyze',
#                              headers = headers,
#                              params = params,
#                              data = image)
#     data = response.json()
#     #print(data)v
#     for tag in data['tags']:
#     	print(tag['name'], tag['confidence'], '\n')


# for profile_pic in os.listdir('chatpps'):
# 	person = profile_pic.split('.')[0]
# 	print(person)
# 	image = open('chatpps/' + profile_pic, 'rb').read()
try:
	response = requests.post(url = 'https://westeurope.api.cognitive.microsoft.com/vision/v1.0/analyze', 
	 	headers = headers, 
	 	params = params, 
	 	data = image)
	data = response.json()
	print(data)
	with open('output/' + person + '.txt', 'w') as outfile: json.dump(data, outfile)

except Exception as e:
	print("[Errno {0}] {1}".format(e.errno, e.strerror))