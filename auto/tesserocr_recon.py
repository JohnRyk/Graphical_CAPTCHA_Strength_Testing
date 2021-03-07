import tesserocr
import requests
from PIL import Image

'''
for c in range(0,100):
	# pull pictures
	f_name = str(c)
	save_path = "./processed/"+f_name+".jpg"
'''


def rec(pic_path):
	# Recon using tesserocr
	image = Image.open(pic_path)
	result = tesserocr.image_to_text(image)
	result = result.split('\n')[0]
	if len(result) > 6:
		result = result[-6:]
	return result