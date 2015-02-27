#coding=utf-8
 

import urllib.request
import re



def getHtml(url):
    page = urllib.request.urlopen(url).decode('utf-8')
    html = page.read()
    return html


def getImg(html):
    reg = r'src="(.+?\.jpg)" pic_ext'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
 #   x = 0
   # request.urlretrieve(imglist[0],'%s.jpg' % 1)
 #   for imgurl in imglist:
 #       if x==0:
 #           request.urlretrieve(imgurl,'%s.jpg' % x)
 #       x+=1
    return imglist


html = getHtml("http://tieba.baidu.com/p/3534391228")
myurl=getImg(html)







