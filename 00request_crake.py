
import urllib
import re
from bs4 import BeautifulSoup
from distutils.filelist import findall

#下面三行是编码转换的功能
#import sys
#reload(sys)
#sys.setdefaultencoding("utf-8")


host = "http://119.29.175.97/c/hdyzma/"

page = urllib.request.urlopen(host)
contents = page.read()
#print(contents)

soup = BeautifulSoup(contents,"html.parser")

#print(soup)
print(soup.find('input',style='display:none')['value'])
#print(soup.input['value'])
#for tag in soup.find_all('form', id='myform'):
#      tokenn = tag.find('token').get_text('value')
 #   print(tag)
  #  tokenn = str(tag)[288:312]
   # print(tokenn)

