#!~/Documents/pythonFiles/venv python
# -*- coding:utf-8 -*-

import time
from appium import webdriver



def safe_alert_click(driver, eles_0):
    if len(eles_0) == 0:
        alert_remove(driver)
        ele = eles_0[0]
        ele.tap()
    else:
        ele = eles_0[0]
        ele.click()




def alert_remove(driver):
    eles = driver.find_elements_by_ios_predicate("type == 'XCUIElementTypeAlert'")
    check_cycle(eles, '系统Alert检测', check_cycle_total_count=1)
    if len(eles) > 0:
        driver.switch_to.alert.accept()

    eles = driver.find_elements_by_ios_predicate("type == 'XCUIElementTypeStaticText' AND name == '发现新版本'")
    check_cycle(eles, '发现新版本')
    if len(eles) > 0:
        ele = driver.find_element_by_ios_predicate("type == 'XCUIElementTypeButton' AND name == '稍后再说'")
        ele.click()


def safe_mask_click(driver, eles_0):
    if len(eles_0) == 0:
        mask_remove(driver)
        ele = eles_0[0]
        ele.tap()
    else:
        ele = eles_0[0]
        ele.tap()



def mask_remove(driver, check_cycle_total_count=3):
    totalCount = check_cycle_total_count

    eles = driver.find_elements_by_ios_predicate("type == 'XCUIElementTypeNavigationBar'")
    check_cycle(eles, '顶部NavigationBar', check_cycle_total_count=1)
    if len(eles) > 0:
        eles_new = driver.find_elements_by_ios_predicate("type == 'XCUIElementTypeNavigationBar' AND enabled = 'true'")

        while len(eles_new) == 0 and totalCount > 0:
            eles[0].tap()
            time.sleep(1)
            totalCount -= 1

        # 点击蒙版次数用尽，则进行一次alert检测
        if totalCount == 0:
            alert_remove(driver)

# 工具方法
def check_cycle(eles, check_title, check_cycle_total_count=3):
    totalCount = check_cycle_total_count
    print('-'*20)
    print("开始检测：%s" % check_title)
    while len(eles) == 0 and totalCount > 0:
        print(f"检测中：{check_title} 计数：{totalCount}" )
        time.sleep(1)
        totalCount -= 1

    if totalCount:
        print("检测到：## %s ##" % check_title)
    print("结束检测：%s" % check_title)

