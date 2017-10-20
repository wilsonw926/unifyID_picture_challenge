#Random Bitmap Image Coding Challenge for UnifyID
#Author: Wilson Wang (github.com/wilsonw926)

import requests
import numpy as np
from PIL import Image

#Constants
RANDOM_ORG_URL = "https://www.random.org/integers/"

IMG_ROW = 128
IMG_COL = 128
TOTAL_PIXELS = IMG_ROW * IMG_COL

#Grabs the random integers from the random.org url with the given params
def grab_random_ints(num):

	#Sample URL: https://www.random.org/integers/?num=10&min=1&max=6&col=1&base=10&format=plain&rnd=new
	#Params for the random.org url
	params = {
		'num': str(num),
	    'min': '0',
	    'max': '255',
	    'col': '3',
	    'base': '10',
	    'format': 'plain',
	    'rnd': 'new'
	}

	r = requests.get(RANDOM_ORG_URL, params=params)
	#Makes sure response is 200
	if r.status_code != 200:
		print(str(r.status_code) + " Error")
		exit()
	else:
		parsed_data = [int(x) for x in r.text.split()]
		return parsed_data

def main():
	grab_random_ints(10)

#execute
main()