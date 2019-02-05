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
    s = 0
    if v == 1:
        time.sleep(1)
        click(1155,60)
        click(850,700)
        time.sleep(2)
        click(850,700)
        time.sleep(1)

        click(940,700)
        time.sleep(1)
        click(940,700)
    else:
        click(220,750)
        time.sleep(2)

        click(850,700)
        time.sleep(3)
        click(850,700)
        time.sleep(2)

        click(940,700)
        time.sleep(1)
        click(940,700)
        time.sleep(1)
        click(100,750)

    while s < t:
        time.sleep(1)
        print t-s, "seconds remaining."
        s+=1
