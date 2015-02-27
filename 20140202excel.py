import xlrd

data = xlrd.open_workbook('F:\工作\企业目录.xls')
table = data.sheets()[0]          #通过索引顺序获取
nrows = table.nrows
ncols = table.ncols



xf = 0
table.put_cell(2, 2, 1, 'okokok', xf)


def display():
    for i in range(nrows):
        for j in range(ncols):
            print(table.cell(i,j).value)
