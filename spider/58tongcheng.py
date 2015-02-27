#coding=utf-8
 
from xlwt3 import *
import urllib.request
import re
import xlwt3 as xlwt
import string




f = Font()
#f.height = 20*72
#f.name = 'Verdana'
#f.bold = True

f.underline = Font.UNDERLINE_SINGLE
f.colour_index = 4

h_style = XFStyle()
h_style.font = f






def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read().decode('utf-8')    
    return html


def getInfo(html,times):     
    #reglist = [r'infoid=".+">(.+?)</a>',r'<b class=\'pri\'>(\d+\.?\d+?) </b> 万']

    if times ==1:
       infoall=[['发布时间','名称','面积（平方）','总价（万）','单价（元/平方）','户型',
              '住宅类别','装修程度','房屋类型','建筑结构','建造年代','房屋楼层','产权','朝向','详细介绍','所属小区']]
    else:
        infoall=[]
    
    

    reg = r'<tr logr=.+?>([\s\S]+?)<br/>\s+</div>\s+</td>\s+</tr>' #整条信息表达式（大段）   
    infore = re.compile(reg)
    infolist = re.findall(infore,html) #整条信息列表
    


    reglist = [r'\s+&nbsp(\S+)',
               r'infoid=".+">(.+?)</a>',
               r'</span>\s+\((\d+(?:\.\d+)?)㎡\)',
               r'<b class=\'pri\'>(\d+(?:\.\d+)?) </b> 万',
               r'(\d+(?:.\d+)?)元/㎡\s+<br/>',
               r'<span class="showroom">\s+(\S+)\s+</span>',
               r'a href="(\S+)" target="_blank" class="t"\s+(rel="nofollow")?\s*infoid=',
               r'>\s*-\s(?:<a.+>)?([^<].+)二手']#内部信息项表达式
    
    for info in infolist:#单条信息(未提取)
        info_ax=[]#单条信息(提取)
        col=0
        for reg in reglist:
            infore = re.compile(reg)
            if col in [2,3,4]:               
                #print(col)
                #print(info_ax[0])
                info_ax.append(float(re.search(infore,info).group(1)))
                
            elif col == 6: 
                info_ax+=getMore(re.search(infore,info).group(1))    
            else:                    
                #print(col)
                #if len(info_ax)>0:
                   # print(info_ax[0])
                if re.search(infore,info)==None:
                    col+=1
                    info_ax.append('None')
                    continue
                info_ax.append(re.search(infore,info).group(1))
            col+=1
        infoall.append(info_ax)        
    return infoall


def getMore(url):    
    html=getHtml(url)
    
    reg = r'<li class="des_cols2">(\S+)</li>'   
    infore = re.compile(reg)
    infolist=re.findall(infore,html) #多项信息列表

    reg=r'<p>(?:<p>)?(.+?)</p>'#详细信息
    infore = re.compile(reg)
    more=re.search(infore,html).group(1)

    
    infore = re.compile(r'(<.+?>)')
    more=infore.sub('', more,count = 10 )

    infore = re.compile(r'(&nbsp;)')
    more=infore.sub('', more,count = 10 )
    
    
    infolist+=[more,url]

    
    return infolist



def writexls(file_name,table_name,data_list):
    book=xlwt.Workbook()
    sheet=book.add_sheet(table_name)    
    row=0
    url="http://www.baidu.com"
    for datarow in data_list:
        
        
        col=0
        for data in datarow:
            #sheet.row(row).write(col,data)          
                
            if col==1 and len(datarow[15])<255 and row>0:
                
                sheet.write(row, col, Formula('HYPERLINK("%s"; "%s")'%(datarow[15],data)),h_style)
                
            elif col==15:
                col+=1
            else:
                sheet.write(row, col, data)               
                
            #print(data)
            col+=1
        row+=1
        
    book.save(file_name)


myinfo=[]
for i in range(1,3):
    html = getHtml("http://nt.58.com/qidong/ershoufang/e3/pn%d/"%i)
    print("http://nt.58.com/qidong/ershoufang/e3/pn%d/"%i)
    myinfo +=getInfo(html,i)

writexls('58d.xls','test',myinfo)






