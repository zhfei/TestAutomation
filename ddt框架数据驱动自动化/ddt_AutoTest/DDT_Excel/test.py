#!~/Documents/pythonFiles/venv python
# -*- coding:utf-8 -*-

# ddt,类装饰器
# data,unpack 方法装饰器

from selenium import webdriver
import unittest
from ddt import ddt,data,unpack

from dataExcel import DataExcel



data_list = DataExcel().getdata()
print(data_list)


@ddt # 类装饰器
class test_se(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('/Users/zhoufei/Documents/测试自动化/Web自动化_Web爬虫/chromedriver')
        self.driver.get("https://passport.ctrip.com/user/login?BackUrl=https%3A%2F%2Fwww.ctrip.com%2F#ctm_ref=c_ph_login_buttom")

    #利用装饰器，data_list中的每个数据都会传到下面的测试方法中
    @data(*data_list) # 当传入下面测试方法test0的参数为一个时,传入list类型的不定长度列表
    @unpack # 如果参数为多个，则需要用unpack装饰器开包一下
    # **dict传入不定长度的dict
    def test0(self, **dict):
        self.driver.find_element_by_id('nloginname').send_keys(dict.get('username'))
        self.driver.find_element_by_id('npwd').send_keys(dict.get('password'))

        print(dict)
        self.assertEqual(dict.get('username'), dict.get('password'))

    def tearDown(self):
        pass



if __name__ == '__main__':
    unittest.main()