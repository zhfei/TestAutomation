#!~/Documents/pythonFiles/venv python
# -*- coding:utf-8 -*-

import yaml

file = open('data.yaml')
result = yaml.load(file,Loader=yaml.FullLoader)
print(result)

file = open('data2.yaml')
result = yaml.load(file, Loader=yaml.FullLoader)
print(result)
print(result['website_order'])