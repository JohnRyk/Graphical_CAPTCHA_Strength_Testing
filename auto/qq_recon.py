import requests
import time
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def qq_rec(pic_name,pic_path):
	#print("[*] Tesing picture: "+pic_name)

	target_url = "https://ai.qq.com:443/cgi-bin/appdemo_handwritingocr?g_tk=5381"
	cookies = {"pgv_pvid": "6955288690", "pgv_pvi": "7347727360", "pt_local_token": "2-", "pgv_info": "ssid=s7707865414", "pgv_si": "s8338437120", "__root_domain_v": ".ai.qq.com", "_qddaz": "QD.7w16gz.fz82ec.kde4ai65", "_qdda": "3-1.1", "_qddab": "3-w2tf0g.kde4aiaw", "_qddamta_2852060660": "3-0"}
	headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0", "Accept": "*/*", "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2", "Accept-Encoding": "gzip, deflate", "Referer": "https://ai.qq.com/product/ocr.shtml", "Origin": "https://ai.qq.com", "Connection": "close"}

	proxy = {'http': 'http://127.0.0.1:8080' ,'https': 'https://127.0.0.1:8080'}

	post_file = {'image_file': (pic_name,open(pic_path,'rb'),'image/jpeg') }
	#res = requests.post(target_url, headers=headers, cookies=cookies, files=post_file, proxies=proxy, verify=False)
	#res = requests.post(target_url, headers=headers, cookies=cookies, files=post_file, verify=False, timeout=5)
	res = requests.post(target_url, headers=headers, files=post_file, verify=False, timeout=5)

	res_data = res.json()

	if res_data['ret'] == 0:
	# response is ok
		#print(res_data)
		recon_result = res_data['data']['item_list'][0]['itemstring']
	else:
	# cannot recon set it to null
		recon_result = ""

	# recon result length longer than 6, remain the last 6
	if len(recon_result) > 6:
		recon_result = recon_result[-6:]

	return recon_result


if __name__ == '__main__':
    output = []
    cycle = 5
    for c in range(0,cycle):
        pic_name = "%s.jpg" %c 
        pic_path = "./pic/%s.jpg" %c 
        res = qq_rec(pic_name,pic_path)
        output.append(res)
    print(output)
