#!~/Documents/pythonFiles/venv python
# -*- coding:utf-8 -*-


from base import base_business_ios, base_tool_ios

from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


# home页面业务
def myconsult_start(driver):
    wait = WebDriverWait(driver,20)
    EC.element_to_be_clickable
    wait.until(EC._element_if_visible(driver.find_element_by_ios_predicate("type == 'XCUIElementTypeStaticText' AND name == '新房'")))

    eles = driver.find_elements_by_ios_predicate("type == 'XCUIElementTypeStaticText' AND name == '新房' AND enabled == 'true'")
    base_business_ios.safe_mask_click(driver, eles)











