#!~/Documents/pythonFiles/venv python
# -*- coding:utf-8 -*-


import requests
# requests有中文的官方文档，可以查找详细用法

import pprint
# pprint格式化打印


# get测试

getRes = requests.get("https://www.baidu.com")

if getRes.status_code == 200:
    print("测试通过!")
else:
    print("测试失败!")

print(getRes.status_code)
#pprint(res.json(), width = 30)




# post测试

postRes = requests.post("https://www.baidu.com", data= {
    'action':'add_course',
    'data':"""
    {
        'name':'猴哥',
        'des':'初中数学',
        'display_index':'4'
    }
    """
})

print(postRes.status_code)

postResObj = postRes.json()["list"]


assert postResObj == None
assert postResObj["name"] == "小明"

print("-"*10 + '测试通过' + "-"*10)