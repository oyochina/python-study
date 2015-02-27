#!/usr/bin/env python
# -*- coding: windows-1251 -*-
# Copyright (C) 2005 Kiseliov Roman

from xlwt3 import *



w = Workbook()
ws = w.add_sheet('F')

##############
## NOTE: parameters are separated by semicolon!!!
##############

n = "HYPERLINK"

url0="http://www.baidu.com"

#url='("http://www.baidu.com";"test")'

url='('+url0+';'+"test"+')'

#ws.write(0, 0, Formula(n + '("http://www.baidu.com";"test")'))
ws.write(0, 0, Formula('HYPERLINK("%s"; "click me")'%url0))

w.save("hyperlinks.xls")

#ttt=n + '("http://www.baidu.com";"test")'
#print(ttt)
