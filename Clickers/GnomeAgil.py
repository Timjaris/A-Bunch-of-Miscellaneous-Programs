import win32api, win32con
import time

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

#zoom out
time.sleep(3)
win32api.keybd_event(0x22, 0,0,0)
time.sleep(3)
win32api.keybd_event(0x22,0 ,win32con.KEYEVENTF_KEYUP ,0)

#face north
click(1050,80)
time.sleep(1)

while 1:
    click(120,410)
    time.sleep(15) #log

    click(675,550)
    time.sleep(6) #net

    click(675,480)
    time.sleep(6) # branch1

    click(610,420)
    time.sleep(7) #branch2

    click(1050,500)
    time.sleep(13) #sign

    click(1180,170) #pole adj
    time.sleep(3)

    click(640,158) #poles
    time.sleep(15)

    click(1240,120)
    time.sleep(6)

    click(500,440)
    time.sleep(10)





