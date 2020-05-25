#!~/Documents/pythonFiles/venv python
# -*- coding:utf-8 -*-

import unittest
from selenium import webdriver
from time import sleep
from ddt import ddt,file_data



@ddt
class Test_Yaml(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('/Users/zhoufei/Documents/测试自动化/Web自动化_Web爬虫/chromedriver')
        self.driver.get(
            "https://passport.ctrip.com/user/login?BackUrl=https%3A%2F%2Fwww.ctrip.com%2F#ctm_ref=c_ph_login_buttom")
        self.driver.implicitly_wait(10)

    @file_data('data.yaml')
    # **kwargs 表示传递的参数是字典类型， **表示参数是字典类型
    def test_1(self, **kwargs):
        username = kwargs.get('username')
        password = kwargs.get('password')
        login_state = kwargs.get('assert')
        self.driver.find_element_by_id('nloginname').send_keys(username)
        self.driver.find_element_by_id('npwd').send_keys(password)

        print(dict)
        ele_text = self.driver.find_element_by_id('successid').text
        self.assertEqual(ele_text,login_state, '状态不符合预期')
        # self.assertEqual(dict.get('username'), dict.get('password'))



    def tearDown(self):
        self.driver.quit()
        pass


if '__main__' == __name__:
    unittest.main()