#import xlrd

#data = xlrd.open_workbook('excelFile.xls')

#table = data.sheets()[0]
#nrows = table.nrows
#ncols = table.ncols

#for i in range(nrows ):
 #   print table.row_values(i)

#value='test'
#ctype = 1
#row = 1
#col = 1
#xf = 0 # 扩展的格式化
#table.put_cell(row, col, ctype, value, xf)

import xlwt3 as xlwt


from datetime import datetime
  
font0 = xlwt.Font()
font0.name = 'Times New Roman'
font0.colour_index = 2
font0.bold = True
  
style0 = xlwt.XFStyle()
style0.font = font0
  
style1 = xlwt.XFStyle()
style1.num_format_str = 'D-MMM-YY'
  
wb = xlwt.Workbook()
ws = wb.add_sheet('A Test Sheet')
  
ws.write(0, 0, 'Test', style0)
ws.write(1, 0, datetime.now(), style1)
ws.write(2, 0, 1)
ws.write(2, 1, 1)
ws.write(2, 2, xlwt.Formula("A3+B3"))
  
wb.save('example.xls')


