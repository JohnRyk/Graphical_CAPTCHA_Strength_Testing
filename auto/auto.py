from PIL import Image
from urllib import request
import requests
import os
import cv2
import time
#from tesserocr_recon import rec
from qq_recon import qq_rec

pic_url = "http://127.0.0.1:9080/ccs_picture/captcha/fetch?reqid=123321"
verify_url = "http://127.0.0.1:9080/ccs_picture/captcha/verify"



def process_pic(pic_path):

	img = Image.open(pic_path)
	save_name = pic_path.split('/')[-1]
	save_path = './processed/'+save_name


	# Pic color to gray
	img_gray = img.convert('L')

	# Pic convert color -> white & white -> black
	img_black_white = img_gray.point(lambda x: 0 if x > 200 else 255)
	# Pic convert black -> white & white -> black
	img_black_white = img_black_white.point(lambda x: 0 if x > 200 else 255)
	img_black_white.save(save_path)

	# opencv handle
	img_cv = cv2.imread(save_path)
	im = cv2.cvtColor(img_cv,cv2.COLOR_BGR2GRAY)
	result_img = cv2.adaptiveThreshold(im, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 1)
	cv2.imwrite(save_path,result_img)


	# clean noise
	img = result_img
	for i in range(0,16):
		h,w = img.shape[:2]
		for y in range(0,w):
			for x in range(0,h):
				if y == 0 or y == w - 1 or x == 0 or x == h - 1:
					img[x,y] = 255
					continue
				count = 0
				if img[x, y - 1] == 255:
					count += 1
				if img[x, y + 1] == 255:
					count += 1
				if img[x - 1, y] == 255:
					count += 1
				if img[x + 1, y] == 255:
					count += 1
				if count > 2:
					img[x, y] = 255
		cv2.imwrite(save_path,img)


	return save_path


all_count = 3
success_count = 0
correct_count = 0

for c in range(0,all_count):
	# pull pictures
	f_name = str(c)
	pic_name = f_name+".jpg"
	save_path = "./pic/"+f_name+".jpg"

	# refresh all pictures
	#request.urlretrieve(pic_url,save_path)

	# return processed picture path
	ret_path = process_pic(save_path)

	# Recon using qq API
	recon_result = qq_rec(pic_name,ret_path)

	# Recon using tesserocr
	#recon_result = rec(ret_path)


	# Count success
	if recon_result != "":
		success_count+=1

	# Verify
	target_url = verify_url
	datas = {}
	datas['reqid'] = '123321'
	datas['input_data'] = recon_result
	res = requests.post(verify_url,timeout=5,data = datas)
	# Count correct
	if res.status_code == 200:
		print("[+] Picture %s -> %s Match!" % (pic_name,recon_result))
		correct_count += 1
	else:
		print("[-] Picture %s -> %s Dose not match." % (pic_name,recon_result))
 
	time.sleep(0.4)


success_rate = (success_count/all_count)*100

correct_rate = (correct_count/all_count)*100

print("------------------------------------------------------------")
print("[+] %d Testing complete.\n\
	[+] %d is success.\n\
	[+] %d is correct.\n\
	[+] The result of the picture recon success rate is: %0.2f percent\n\
	[+] The result of the picture recon correct rate is: %0.2f percent" % (all_count,success_count,correct_count,success_rate,correct_rate))



