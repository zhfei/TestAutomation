#!~/Documents/pythonFiles/venv python
# -*- coding:utf-8 -*-


from appium import webdriver

from base import base_business_ios
from business import login_business_ios, home_business_ios


desired_caps = {}
desired_caps['platformName'] = 'iOS'
desired_caps['platformVersion'] = '13.3'
desired_caps['deviceName'] = 'iPhone 11'
desired_caps['app'] = 'xxx.app'
desired_caps['automationName'] = 'XCUITest'
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True
desired_caps['noReset'] = True
desired_caps['newCommandTimeout'] = 6000
# desired_caps['automationName'] = 'uiautomator2'


# 启动Remote RPC
driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)

#----------------统一设置-----------------
#所有弹窗默认允许
# driver.switch_to.alert.accept()


# 等待
#隐式等待：针对全部元素设置的等待时间 (不出现就异常崩溃)
# driver.implicitly_wait(10)
# 显示等待：针对某个元素来设置的等待时间
# element = WebDriverWait(driver, 5).until(lambda x: x.find_element_by_id("someId"))
# 强制等待：
# time.sleep(5)

#----------------app引导和登录-----------------

# 处理引导页
base_business_ios.alert_remove(driver)
login_business_ios.app_guide(driver)

# 处理引导页后的弹窗
base_business_ios.alert_remove(driver)
login_business_ios.app_check(driver)

# 登录
base_business_ios.alert_remove(driver)
login_business_ios.app_login(driver)


#----------------Home-----------------
home_business_ios.myconsult_start(driver)

# ele = driver.find_element_by_ios_predicate("type == 'XCUIElementTypeButton' AND name == '登录'")






