import win32api, win32con
import time, fun, math

start = time.time()

win32api.keybd_event(0xBA  ,0 ,0)
while (time.time()-start) < 3600:
    fun.click(1840, 1015)
    time.sleep(.5)
    fun.click(1431, 676)
    time.sleep(10)
    fun.printTime(time.time()-start)
    
win32api.keybd_event(0xBA  ,0 ,0)
