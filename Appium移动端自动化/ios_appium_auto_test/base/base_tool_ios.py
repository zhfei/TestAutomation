#!~/Documents/pythonFiles/venv python
# -*- coding:utf-8 -*-

from appium import webdriver


swipe_duration = 0.3

def swipe_Down(driver):
    window_size = driver.get_window_size()
    width = window_size.get("width")
    height = window_size.get("height")
    driver.execute_script("mobile:dragFromToForDuration",
                         {"duration": swipe_duration, "element": None, "fromX": width / 2, "fromY": height / 4, "toX": width / 2,
                           "toY": height * 3 / 4})

def swipe_Up(driver):
    window_size = driver.get_window_size()
    width = window_size.get("width")
    height = window_size.get("height")
    driver.execute_script("mobile:dragFromToForDuration",
                         {"duration": swipe_duration, "element": None, "fromX": width/2, "fromY": height/4, "toX": width/2,
                          "toY": height*3/4})

def swipe_Left(driver):
    window_size = driver.get_window_size()
    width = window_size.get("width")
    height = window_size.get("height")
    driver.execute_script("mobile:dragFromToForDuration",
                         {"duration": swipe_duration, "element": None, "fromX": width*3/ 4, "fromY": height / 4,
                          "toX": width / 4,
                          "toY": height / 4})

def swipe_Rigth(driver):
    window_size = driver.get_window_size()
    width = window_size.get("width")
    height = window_size.get("height")
    driver.execute_script("mobile:dragFromToForDuration",
                          {"duration": swipe_duration, "element": None, "fromX": width / 4, "fromY": height / 4,
                           "toX": width *3 / 4,
                           "toY": height / 4})


