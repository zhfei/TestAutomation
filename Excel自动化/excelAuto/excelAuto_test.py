#!~/Documents/pythonFiles/venv python
# -*- coding:utf-8 -*-

# xls 与 xlsx的读写方式不同


# 1、使用xlrd模块对xls文件进行读操作
# 2、使用xlwt模块对xls文件进行写操作
# 3、使用openpyxl模块对xlsx文件进行读操作
# 4、使用openpyxl模块对xlsx文件进行写操作
# 5、修改已经存在的工作簿(表)



# xls读写
import xlwt
import xlrd #读取excl表格
from xlutils.copy import copy #复制函数 xls xlsx

#网络请求
import requests
import json




# 读取测试用例

excelDir = u'/Users/zhoufei/Documents/接口自动化/Excel自动化/excel自动化测试.xlsx'
# 1打开excel
workbook = xlrd.open_workbook(excelDir)
# 2查看所有的子表名
sheet_names = workbook.sheet_names()
print(sheet_names)
print(sheet_names[1])

work_sheet = workbook.sheet_by_name('接口文档')

#读取一行
rows = work_sheet.row_values(rowx=1)
print(rows)

#读取一列
clos = work_sheet.col_values(colx=0)
print(clos)

#读取一个cell
cell = work_sheet.cell(rowx=2,colx=5)
print(cell)

#判断一个cell类型: 1:string
print(work_sheet.cell(rowx=2,colx=5).ctype)






# 构建接口对应请求
#
# # 1.获取token
# token_url = 'http://47.96.181.17:9090/rest/toController'
# token_data = {'username':'J201903070064','password':'362387359'}
# token_headers = {'Content-Type':'application/json'}
# respon = requests.post(token_url,data=json.dumps(token_data),headers=token_headers)
# token = respon.json()['token']
# print(token)
#
# # 2.新增用户
# addUser_url = 'http://47.96.181.17:9090/rest/ac01CrmController'
# addUser_data = json.loads(cell) # 将字符串转成json
# print(type(addUser_data))
#
# addUser_headers = {'Content-Type':'application/json','X-AUTH-TOKEN':token}
# addUser_response = requests.post(addUser_url, data=json.dumps(token_data),headers=addUser_headers)
# print(addUser_response.text)
#
#
# res = addUser_response.json()['message']
# if res == '成功':
#     print('新增操作成功！，耗时为：',addUser_response.elapsed.total_seconds())
#     excel_res = 'pass'
# else:
#     print('新增操作失败')
#     excel_res = 'false'





# 测试结果写入excel (xls方式)
excel_res = 'pass'
workbook_r = xlrd.open_workbook(excelDir)
sheet_r = workbook_r.sheet_by_index(0)

workbookWr_w = copy(workbook_r)
sheet_w = workbookWr_w.get_sheet(0)
sheet_w.write(1,9, excel_res)
workbookWr_w.save('/Users/zhoufei/Documents/接口自动化/Excel自动化/excel自动化测试_res.xlsx')















