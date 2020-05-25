#!~/Documents/pythonFiles/venv python
# -*- coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# 通知驱动打开Chrome浏览器
driver = webdriver.Chrome('/Users/zhoufei/Documents/Chrome/chromedriver')
# 元素找不到就等待10s
driver.implicitly_wait(10)


# 通知驱动打开网址：https://www.51job.com/
driver.get('https://www.51job.com/')

#找到搜索框，输入关键词
ele = driver.find_element_by_id('kwdselectid')
ele.send_keys('python')

#找到定位按钮
ele = driver.find_element_by_id('work_position_input')
ele.click()

#将之前所有已经被选择的项，重新再次点击一下，让它们都取消点击（通过css级联表达式搜索）
eles = driver.find_elements_by_css_selector('#work_position_click_center_right_list_000000 em[class=on]')
for ele in eles:
    ele.click()

#找到杭州，点击
ele = driver.find_element_by_id('work_position_click_center_right_list_category_000000_080200')
ele.click()

#点击"确定"按钮，完成位置定位
ele = driver.find_element_by_id('work_position_click_bottom_save')
time.sleep(2) #弹窗按钮，要等几秒才能点击
ele.click()
# ele.send_keys(Keys.ENTER)

#点击"搜索"
ele = driver.find_element_by_css_selector('body > div.content > div > div.fltr.radius_5 > div > button')
ele.click()

#获取所有结果列表
eles = driver.find_elements_by_css_selector("#resultList [class='el']")
for ele in eles:
    text1 = ele.find_element_by_css_selector("p > span > a")
    text2 = ele.find_element_by_css_selector("span > a")
    text3 = ele.find_element_by_css_selector("[class='t3']")
    text4 = ele.find_element_by_css_selector("[class='t4']")
    text5 = ele.find_element_by_css_selector("[class='t5']")
    print(text1.text+'---'+text2.text+'---'+text3.text+'---'+text4.text+'---'+text5.text)

