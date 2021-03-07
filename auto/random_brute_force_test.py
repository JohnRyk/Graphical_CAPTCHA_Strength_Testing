import requests
import random

pic_url = "http://127.0.0.1:9080/ccs_picture/captcha/fetch?reqid=123321"
verify_url = "http://127.0.0.1:9080/ccs_picture/captcha/verify"


def get_random_six():
	string = ""
	for i in range(6):
	    ch = chr(random.randrange(ord('0'), ord('9') + 1))
	    string += ch
	return string


all_count = 5000
success_count = 0

# single
#requests.get(pic_url)

for i in range(0,all_count):
	target_url = verify_url
	datas = {}
	payload = get_random_six()
	datas['reqid'] = '123321'
	datas['input_data'] = payload
	try:
		# multi
		requests.get(pic_url)
		res = requests.post(verify_url,timeout=5,data = datas)
	except:
		pass
	# Count
	if res.status_code == 200:
		print("[%d] Trying %s -> correct !" % (i,payload))
		success_count += 1
	else:
		print("[%d] Trying %s -> failed." % (i,payload))

print("------------------------------------------------------------")
print("[+] %d Testing complete.\n\
	[+] %d is success.\n\
	[+] The result of the picture recon correct rate is: %0.2f percent" % (all_count,success_count,(success_count/all_count)*100))