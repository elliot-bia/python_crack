#coding:utf-8

import urllib
import re
from bs4 import BeautifulSoup
from distutils.filelist import findall

import requests



host = "http://打码用***打码用/c/hdyzma/"

page = urllib.request.urlopen(host)
contents = page.read()

soup = BeautifulSoup(contents,"html.parser")
#soup的用法
token = soup.find('input',style='display:none')['value']
print(token)
#这里用法 是  find后面一个参数是标签，然后找到特殊的字符‘style=none’，最后获取其中的value值


url = host+'welcome.php'
d = {'name': 'admin', 'token': token }
r = requests.post(url, data=d)
r.encoding = 'UTF-8'
print(r.text)
