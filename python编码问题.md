```txt
Unicode 相互转化
str=u"中单没有保护"
test = open("C:\Users\lenovo\Desktop\\tes\\test.txt", "a")
print type(str) #Medium转为中	
print str
str=str.encode("unicode_escape").decode("string_escape")
# str=str.decode("unicode_escape")
print type(str)
print str
test.write(str.decode("unicode_escape"))


loc=u'哈喽'
a=(loc.encode("unicode_escape").decode("string_escape")).decode('unicode-escape').encode('utf-8')
print a,'|||type:',type(a)


utf8转gbk
str.decode('UTF-8').encode('GBK')

html GB2312转utf-8
if __name__ == "__main__":
    r = urllib2.urlopen("https://121.12.137.98").read()
    r=unicode(r, "gb2312").encode("utf8")
    print r

1.向普通文本文件写入Unicode字符
python内置库中的open方法只能读写ascii码，如果想写入Unicode字符，需要使用codecs包
代码示例：
# -*- coding: utf-8 -*-
import codecs
content = u'你好'
f = codecs.open('c:/test.txt', 'w', 'utf-8')
f.write(content)


gbk转unicode
from array import array

def decode_gbk2_unicode(a):
    b = array('u', a)
    c = b.tostring()
    d = c[::2]
    e = d.decode('gbk')
    return e
		
def main():

    a= u'\xCD\xF5\xD3\xC2'
    a=decode_gbk2_unicode(a)
    print a
    type(a)
if __name__ == '__main__' :
    main()
    pass
```

