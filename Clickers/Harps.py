import win32api, win32con
import time, fun, math

start = time.time()

win32api.keybd_event(0xBA  ,0 ,0)
while (time.time()-start) < 3600:
    fun.click(1213, 537)
    time.sleep(30)
    
win32api.keybd_event(0xBA  ,0 ,0)
