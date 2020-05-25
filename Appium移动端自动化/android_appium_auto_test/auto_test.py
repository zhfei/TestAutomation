#!~/Documents/pythonFiles/venv python
# -*- coding:utf-8 -*-

from appium import webdriver
import time,traceback


desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '9'
desired_caps['deviceName'] = 'test'
desired_caps['app'] = '/Users/zhoufei/Documents/测试自动化/Appium移动端自动化/toutiao359.apk'
desired_caps['appPackage'] = 'io.manong.developerdaily'
desired_caps['appActivity'] = 'io.toutiao.android.ui.activity.LaunchActivity'
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True
desired_caps['noReset'] = True
desired_caps['newCommandTimeout'] = 6000
# desired_caps['automationName'] = 'uiautomator2'


# 启动Remote RPC
driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)

try:
    driver.implicitly_wait(10)

    # 根据id找元素，并点击
    driver.find_element_by_id('io.manong.developerdaily:id/tab_bar_plus').click()
    time.sleep(1)
    driver.find_element_by_id('io.manong.developerdaily:id/btn_email').click()
    time.sleep(1)

    # 输入用户名，密码
    ele = driver.find_element_by_id('io.manong.developerdaily:id/btn_email')
    ele.send_keys('jcyrss@163.com')

    ele = driver.find_element_by_id('io.manong.developerdaily:id/edt_password')
    ele.send_keys('sdfsdf')
    time.sleep(2)

    # 点击登录
    driver.find_element_by_id('io.manong.developerdaily:id/btn_login').click()

except:
    print(traceback.format_exc())

input('****Press to quit...')
