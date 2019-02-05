import win32api, win32con
import time

def click(x,y):
    a,b = win32api.GetCursorPos()
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
    win32api.SetCursorPos((a,b))
    
t = 51
v=1

while 1:
    click(1408, 559)
    print "click"
    time.sleep(5)
    
    
