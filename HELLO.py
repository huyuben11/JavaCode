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
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = 'com.android.settings.Settings'
#测试脚本中输入时需要输入中文，则必须设置为true  输入法为appium的输入法
desired_caps['unicodeKeyboard'] = 'True'
#测试结束时，输入法为系统输入法
desired_caps['resetKeyboard'] = 'True'
#设置新的超时时间（用作延长超时时间）/超时时间为100秒
desired_caps['newCommandTimeout'] = '100'

# 获取driver
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(5)
driver.get_window_size()
print(driver.available_ime_engines)

# text="日期和时间"
#当前界面无元素，需要通过下拉查找
#通过下拉查找到子元素的       className为android.widget.TextView，且text值为日期和时间，true 表示允许滑动
# element=driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().scrollable(true)).getChildByText(new UiSelector().className(android.widget.TextView),"%s")' %text)
# element.click()
#element=driver.find_element_by_android_uiautomator('new UiSelector().text("%s")' %text)

# screenAwakevalue='mAwake=true\n'
#
# allList = os.popen('adb shell input keyevent 3').readlines()
# print(allList)
# if  len(allList):
#     print('屏幕已灭屏')
# else:
#     print('屏幕已点亮')

# driver.press_keycode(6)
# 操作通知栏
# driver.open_notifications()
# def getSize():
#     x = driver.get_window_size()['width']
#     y = driver.get_window_size()['height']
#     return (x, y)


# def swipeUp(t):
#     l = getSize()
#     x1 = int(l[0] * 0.5)    #x坐标
#     y1 = int(l[1] * 0.75)   #起始y坐标
#     y2 = int(l[1] * 0.25)   #终点y坐标
#     time.sleep(1)
#     driver.swipe(x1, y1, x1, y2,t)
# #向下滑动
# swipeUp(1000)
# time.sleep(3)
# 添加智能设备
# driver.find_element_by_id("com.loctek.ble:id/iv_empty").click()





#通过位置进行点击
# # 创建对象（用于特殊动作）
# touch_action=TouchAction(driver)
# touch_action.press(x=522,y=1378).release().perform()
# time.sleep(1)
# touch_action.press(x=791,y=1952).release().perform()
# time.sleep(1)
# # driver.find_element_by_xpath("//*[text='升降桌']").click()
# touch_action.press(x=617,y=441).release().perform()
# time.sleep(3)
# # driver.find_element_by_id("com.loctek.ble:id/cl_item").click()
# # 附近蓝牙设备点击
# driver.find_element_by_id("com.loctek.ble:id/ll_item").click()
# time.sleep(1)
# # 开始体验
# driver.find_element_by_id("com.loctek.ble:id/tv_submit").click()
# time.sleep(1)
# # 上升
# # touch_action.long_press(x=716,y=1292,duration=600).perform()
# # 下降
# touch_action.long_press(x=355,y=1292,duration=12000).perform()
# time.sleep(2)
# # 下降停止
# touch_action.press(x=355,y=1292).release().perform()


# touch_action.press(a).release().perform()
# a.send_keys("aaaaa")
# a.click()

# 进入后台5秒，再回到前台
# driver.start_activity("com.imbb.banban.android",".MainActivity")

# print("---- 已经回到前台 ----")

# driver.quit()

#-----------------------------------------------------------#
# 打开一个文件
# class Employee:
#     '所有员工的基类'
#     empCount = 0
#
#     #初始化方法
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#         Employee.empCount += 1
#
#     def displayCount(self):
#         print("Total Employee %d" % Employee.empCount)
#
#     def displayEmployee(self):
#         print("Name : ", self.name, ", Salary: ", self.salary)
#
#
# "创建 Employee 类的第一个对象"
# emp1 = Employee("Zara", 2000)
# "创建 Employee 类的第二个对象"
# emp2 = Employee("Manni", 5000)
# emp1.displayEmployee()
# emp2.displayEmployee()
# print("Total Employee %d" % Employee.empCount)

# -------------------#
# 为线程定义一个函数
# def sing():
#     for i in range(3):
#         print("正在唱歌...%d"%i)
#
# def dance():
#     for i in range(3):
#         print("正在跳舞...%d"%i)
#
# t1 = threading.Thread(target=sing)
# t2 = threading.Thread(target=dance)
#
# t1.start()
# t2.start()
#
# print('---结束---:%s',time.time())

# for i in range(5):
#     print("数字" , i)


# 创建两个线程
# except:
#     print( "Error: unable to start thread")