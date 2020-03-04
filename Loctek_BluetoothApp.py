from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time
import threading
import os

desired_caps = dict()
# 手机参数
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '9'
desired_caps['deviceName'] = ' devices'
# 应用参数
desired_caps['appPackage'] = 'com.loctek.ble'
desired_caps['appActivity'] = 'com.loctek.ble.gui.devices.DevicesFragment'
# com.loctek.ble.gui.devices.DevicesFragment
# 获取driver
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(5)

# 添加智能设备
driver.find_element_by_id("com.loctek.ble:id/iv_empty").click()
#通过位置进行点击
# # 创建对象（用于特殊动作）
touch_action=TouchAction(driver)

# 基础操作
def BasicOperation():
    # 添加设备
    touch_action.press(x=522, y=1378).release().perform()
    time.sleep(1)
    # 允许打开蓝牙
    touch_action.press(x=535, y=1486).release().perform()
    time.sleep(1)
    # 确定
    touch_action.press(x=800, y=2189).release().perform()
    time.sleep(3)

    # driver.find_element_by_id("com.loctek.ble:id/ll_item").click()
    # 添加新设备
    touch_action.press(x=461, y=1480).release().perform()
    time.sleep(18)
    # 附近蓝牙设备点击
    touch_action.press(x=227, y=501).release().perform()
    time.sleep(3)
    # 开始体验
    # driver.find_element_by_id("com.loctek.ble:id/tv_submit").click()
    touch_action.press(x=504, y=1780).release().perform()
    time.sleep(1)

def Up():
    touch_action.long_press(x=716,y=1292,duration=200).perform()
    time.sleep(1)

def Down():
    touch_action.long_press(x=355, y=1292, duration=200).perform()
    time.sleep(1)

BasicOperation()
for index in range(7):
    print("循环"+index+"次")
    # 偶数上升
    if index % 2 == 0:
        Up()
    # 奇数下降
    else:
        Down()

driver.quit()