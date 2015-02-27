import xlrd
data = xlrd.open_workbook('excelFile.xls')

table = data.sheets()[0]
nrows = table.nrows #行数
ncols = table.ncols #列数

result=(nrows,ncols)
print(result)

rownames =  table.row_values(0)
colnames =  table.col_values(0)

print(colnames)

