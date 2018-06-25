import requests
from bs4 import BeautifulSoup
import os
import threading
import time
print("=========================")
print("孤独常伴    www.0xss.cn")        
print("=========================")
s=input("单个检测:1\n批量检测:2\n请选择:")
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'}
waf=['不存在','找不到','未找到','防火墙','error','go away','so serious','not found','forbidden','access deny','access denied']
def scan():
	if s=="1":
		url=input("URL：")
		o=open("url.txt","r")
		for i in o.readlines():
			urls=url.rstrip('/')+i
			r=requests.get(url=urls,headers=headers)
			if r.status_code==200 or r.status_code == 500:
				print(urls+"存在漏洞\n")
				exit()
			else :
				print(urls+"不存在漏洞\n")
	elif s=="2":
		print("请将需要检测的URL放在该脚本根目录")
		r=input("请输入文件名:")
		o=open("url.txt","r").read().split('\n')
		w=open('{0}'.format(r),"r").read().split('\n')
		for pdd in o:
			for pdw in w:
				urls=pdw+pdd
				try:
					k=requests.get(url=urls,headers=headers)
					if k.status_code==200 or k.status_code == 500:
						one=[]
						one.append(k.url)
						for hh in waf:
							for hx in one:
								fww=requests.get(url=hx,headers=headers)
								if hh in str(fww.text):
									pass
								elif hh not in str(fww.text):
									with open("result.txt","a") as op:
										print("[+]Url:"+fww.url)
										op.write(fww.url)
										op.write('\n')
										op.close()
										exit()
						
				except:
					pass
m=threading.Thread(target=scan)
m.start()
