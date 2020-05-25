#!~/Documents/pythonFiles/venv python
# -*- coding:utf-8 -*-

import xlrd

class DataExcel(object):

    def getdata(self):
        path = 'testdata.xlsx'
        book_work = xlrd.open_workbook(path)
        book_sheet = book_work.sheet_by_index(0)

        rows_num = book_sheet.nrows # 行数
        row0_cells = book_sheet.row_values(0) # 第一行作为字典的键
        cols_num = len(row0_cells)

        info_list = []
        # 第0行为key, 下面的行为value
        for i in range(1,rows_num):
            row_cells = book_sheet.row_values(i)

            dict = {}
            # 遍历列
            for j in range(cols_num):
                dictkey = row0_cells[j]
                dict[dictkey] = row_cells[j]

            info_list.append(dict)

        return info_list
