#!~/Documents/pythonFiles/venv python
# -*- coding:utf-8 -*-

from appium import webdriver
from base import base_business_ios, base_tool_ios


# app 开机引导
def app_guide(driver):
    screen_width = driver.get_window_size()['width']
    screen_height = driver.get_window_size()['height']

    predicateStr = f"type == 'XCUIElementTypeScrollView'"
    eles = driver.find_elements_by_ios_predicate(predicateStr)
    base_business_ios.check_cycle(eles, '引导页', check_cycle_total_count=3)

    isGuide = False
    for i in range(len(eles)):
        ele = eles[i]
        if ele.rect['height'] == screen_height and ele.rect['width'] == screen_width and ele.rect['x'] == 0 and ele.rect['y'] == 0:
            isGuide = True
            break

    if isGuide:
        # 滑动进入app
        leftNum = 3
        while leftNum > 0:
            base_tool_ios.swipe_Left(driver)
            leftNum -= 1

        # 立即体验
        expBtn = driver.find_element_by_ios_predicate(
            "type == 'XCUIElementTypeButton' AND name == 'button_enter'")
        expBtn.click()


# app 登录
def app_login(driver):
    eles = driver.find_elements_by_ios_predicate("type == 'XCUIElementTypeTextField' AND value == '登录名或手机号'")
    if len(eles) > 0:
        ele = eles[0]
        ele.send_keys('88888886666')

        ele = driver.find_element_by_ios_predicate("type == 'XCUIElementTypeSecureTextField' AND value == '密码'")
        ele.send_keys('123456')

        ele = driver.find_element_by_ios_predicate("type == 'XCUIElementTypeButton' AND name == '登录'")
        ele.click()

