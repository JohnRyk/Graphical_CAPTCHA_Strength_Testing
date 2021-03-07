import requests
import time
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


target_url = "https://ai.qq.com:443/cgi-bin/appdemo_handwritingocr?g_tk=5381"
cookies = {"pgv_pvid": "6955288690", "pgv_pvi": "7347727360", "pt_local_token": "2-", "pgv_info": "ssid=s7707865414", "pgv_si": "s8338437120", "__root_domain_v": ".ai.qq.com", "_qddaz": "QD.7w16gz.fz82ec.kde4ai65", "_qdda": "3-1.1", "_qddab": "3-w2tf0g.kde4aiaw", "_qddamta_2852060660": "3-0"}
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0", "Accept": "*/*", "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2", "Accept-Encoding": "gzip, deflate", "Referer": "https://ai.qq.com/product/ocr.shtml", "Origin": "https://ai.qq.com", "Connection": "close"}

#proxy = {'http': 'http://127.0.0.1:8080' ,'https': 'https://127.0.0.1:8080'}

pic_name_list = []
result_list = []
real_list = []

for i in range(0,21):
	file_path = "./pic/"+str(i)+".jpg"
	#file_path = "./processed/"+str(i)+".jpg"
	file_name = str(i)+".jpg"
	pic_name_list.append(file_name)
	post_file = {'image_file': (file_name,open(file_path,'rb'),'image/jpeg') }
	#res = requests.post(target_url, headers=headers, cookies=cookies, files=post_file, proxies=proxy, verify=False)
	res = requests.post(target_url, headers=headers, cookies=cookies, files=post_file, verify=False)

	res_data = res.json()

	if res_data['ret'] == 0:
	# response is ok
		print("[*] Posting file name: "+str(file_name))
		#print(res_data)
		recon_result = res_data['data']['item_list'][0]['itemstring']
	else:
	# cannot recon set it to null
		recon_result = ""
		result_list.append(recon_result)

	# recon result length longer than 6, remain the last 6
	if len(recon_result) > 6:
		recon_result = recon_result[-6:]

	result_list.append(recon_result)
	time.sleep(0.5)

# Generate a dict file_name => recon_result
recon_dict = dict(zip(pic_name_list,result_list))

# Read real_result from real.txt
with open('./real.txt') as f:
	real_list = f.readlines()

# Generate a dict file_name => real_result
real_dict = dict(zip(pic_name_list,real_list))


print(recon_dict)
print(real_dict)
all_count = 0
correct_count = 0
for key,val in real_dict.items():
	all_count += 1
	if val.rstrip("\n") == recon_dict[key]:
		correct_count += 1 

print("[+] %d Testing complete.\n\
	[+] %d is correct.\n\
	[+] The result of the picture recon correct rate is: %f" % (all_count,correct_count,(correct_count/all_count)))

