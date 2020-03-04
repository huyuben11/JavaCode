from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time
import threading
import os

desired_caps = dict()
# 手机参数
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5'
desired_caps['deviceName'] = ' device'
# 应用参数
desired_caps['appPackage'] = 'com.loctek.ble'
desired_caps['appActivity'] = 'com.loctek.ble.gui.MainActivity'

# 获取driver
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(5)

# 添加智能设备
driver.find_element_by_id("com.loctek.ble:id/iv_empty").click()
#通过位置进行点击
# # 创建对象（用于特殊动作）
touch_action=TouchAction(driver)