import win32api, win32con
import time, fun, math

start = time.time()

win32api.keybd_event(0xBA  ,0 ,0)
while (time.time()-start) < 6*3600:
    fun.nats()
    
win32api.keybd_event(0xBA  ,0 ,0)
