#!/bin/env python3
import http.client, urllib.request, urllib.parse, urllib.error, base64
import jsonreader

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': jsonreader.mscv_key,
}

params = urllib.parse.urlencode({
})

try:
    conn = http.client.HTTPSConnection('westeurope.api.cognitive.microsoft.com')
    conn.request("POST", "/vision/v1.0/tag?%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

def get_image_tags(image_path):
	headers = {
	"Content"
	}