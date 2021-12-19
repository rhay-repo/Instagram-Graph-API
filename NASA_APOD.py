'''
Author: Reagan Hay
tools: requests, json, NASA API

'''

import requests
import json

## url
url = 'https://api.nasa.gov/planetary/apod?api_key='

## key
key = #PASTE YOUR KEY HERE#

## retrieve all APOD data
r = requests.get(url + key)

## save json data
json_data = r.json()

## retrieve JUST the image

## parse through the headers for the url
for header in json_data:
	if header == 'url':
		# save the url of the image
		image_url = json_data[header]

## save the image
image = requests.get(image_url)

## get the name of the image
filename = image_url[38:]

## open the file and write the image to it
file = open(filename, "wb")
file.write(image.content)
file.close()