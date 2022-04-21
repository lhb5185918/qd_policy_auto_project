import xlrd
import openpyxl
import os
def get_case(filename,sheetname):
    wb = xlrd.open_workbook(filename=filename)
    sheet = wb.sheet_by_name(sheetname)
    list1 = []
    case = []
    key = sheet.row_values(0)
    for i in range(1,sheet.nrows):
        d = []
        res = sheet.row_values(i)
        for a in res :
            d.append(a)
        list1.append(d)
        for s in list1:
            r = dict(zip(key,s))
        case.append(r)
    return case



