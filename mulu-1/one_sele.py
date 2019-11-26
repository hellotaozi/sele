#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from selenium import webdriver
import time
from selenium.webdriver import ActionChains

driver_in = webdriver.Chrome("/Users/zouyutao/Downloads/chromedriver")
print("step 1: open baidu")
driver_in.get("https://www.baidu.com/")
driver_in.maximize_window()
# driver_in.set_window_size(1600, 900)
time.sleep(5)

print("step 2: open news")
driver_in.find_element_by_name("tj_trnews").click()
# driver_in.find_element_by_link_text("hao123") #跳转出错，为data；
time.sleep(5)

print("step 3: back to baidu")
driver_in.back()
time.sleep(5)

print("step 4: forward to news")
driver_in.forward()
time.sleep(5)

print("step 5: refresh")
driver_in.refresh()
time.sleep(5)

#使用百度搜索
driver_in.get("https://www.baidu.com/")
ele = driver_in.find_element_by_id("kw")
ele.send_keys("selenium")
ele.submit()

# driver_in.find_element_by_css_selector("#su").click()
time.sleep(10)
driver_in.find_element_by_id("kw").clear()

driver_in.find_element_by_xpath("//input[@name='wd']").send_keys("测试策略")
driver_in.find_element_by_xpath("//input[@class='bg s_btn']").click()
time.sleep(30)

#webdriver常用方法：clear()，send_keys(value),click(),submit(),size(),text(),get.attribute(name),is_displayed()
driver_in.get("https://www.baidu.com/")
print(driver_in.find_element_by_css_selector(".s_ipt").size)
print(driver_in.find_element_by_css_selector("#cp").text)
print(driver_in.find_element_by_id("kw").get_attribute("type"))
print(driver_in.find_element_by_id('kw').is_displayed())

#鼠标操作
driver_in.get("https://www.baidu.com/")
above=driver_in.find_element_by_link_text("设置") #定位到要悬停到元素
ActionChains(above).move_to_element(above).perform() #对定位对元素执行鼠标悬停操作


driver_in.quit()
