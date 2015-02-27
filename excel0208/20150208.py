import xlrd
import xlwt3 as xlwt

def readxls(file_name,table_index):
    data = xlrd.open_workbook(file_name)
    table = data.sheets()[table_index]
    nrows = table.nrows #行数
    ncols = table.ncols #列数
 
    list_index=[]
    for ncol in range(ncols):
        list_index.append(table.col_values(ncol))

    list_result=[]
    for nrow in range(nrows):
        list_result.append(table.row_values(nrow))
    
    return list_index,list_result


def writexls(file_name,table_name,data_list):
    book=xlwt.Workbook()
    sheet=book.add_sheet(table_name)
    row=0

    for datarow in data_list:
        col=0
        for data in datarow:
            sheet.row(row).write(col,data)
            col=col+1
        row=row+1
        
    book.save(file_name)




    
llist=readxls('excelFile.xls',0)
print(llist[0])
print(llist[1])

writexls('mytest.xls','test',llist[1])




