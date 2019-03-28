import urllib
import re
from bs4 import BeautifulSoup
from distutils.filelist import findall

host = "http://119.29.175.97/c/hdyzma/"

page = urllib.request.urlopen(host)
contents = page.read()

soup = BeautifulSoup(contents,"html.parser")
#soup的用法

print(soup.find('input',style='display:none')['value'])
#这里用法 是  find后面一个参数是标签，然后找到特殊的字符‘style=none’，最后获取其中的value值