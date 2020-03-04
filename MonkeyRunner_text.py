# -*- coding: UTF-8 -*-
from com.android.monkeyrunner import MonkeyRunner,MonkeyDevice,MonkeyImage
#连接设备
device=MonkeyRunner.waitForConnection()
package ='com.android.settings'
activity = 'com.android.settings.Settings'
component = package +'/'+ activity
#开启应用
device.startActivity(component)
MonkeyRunner.sleep(2)
print('start success')

#滑动
#device.drag((284,1299),(284,315), 1)

#点击
# device.touch(851,102,'DOWN_AND_UP')
# device.touch(199,124,'DOWN_AND_UP')
#输入文本
# device.type('helloworld')

print('touch success')
MonkeyRunner.sleep(3)
#截图
result = device.takeSnapshot()
result.writeToFile('D:\MonkeyRunner\TEST.png','png')