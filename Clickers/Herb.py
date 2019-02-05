import win32api, win32con
import time, fun, math

start = time.time()

win32api.keybd_event(0xBA  ,0 ,0)
while (time.time()-start) < 3600:
    fun.click(1431, 787)
    time.sleep(1)
    fun.click(1091, 1003)
    time.sleep(.5)
    fun.click(1647, 784)
    time.sleep(.5)
    fun.click(1441, 639)
    time.sleep(18)
    
win32api.keybd_event(0xBA  ,0 ,0)
