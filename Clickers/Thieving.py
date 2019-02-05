import win32api, win32con
import time


def click(x,y):
    a,b = win32api.GetCursorPos()
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
    time.sleep(.1)
    win32api.SetCursorPos((a,b))
    time.sleep(0) # increase to 10 if there is lots of lag

def click2(x,y):
    win32api.SetCursorPos((x,y))

a = 701
while 1:
    a,b = win32api.GetCursorPos()
    while a > 700:
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0,0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0,0,0)
        a,b = win32api.GetCursorPos()
        time.sleep(.5)
        click(a,b+40)
        time.sleep(.5)
