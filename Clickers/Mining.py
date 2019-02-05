import win32api, win32con
import time, random


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

def randclick(x,y):
    a,b = win32api.GetCursorPos()
    x = x + random.randint(-1,1)
    y = y + random.randint(-1,1)
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
    time.sleep(.1)
    win32api.SetCursorPos((a,b))
    time.sleep(10*random.random()) # increase to 10 if there is lots of lag
    
def setup():
    #select rs
    click(100,750)
    time.sleep(1)
    click(220,750)
    time.sleep(3)

    #zoom out
    win32api.keybd_event(0x22, 0,0,0)
    time.sleep(3)
    win32api.keybd_event(0x22,0 ,win32con.KEYEVENTF_KEYUP ,0)

    #face north
    click(1110,80)

    #Select Inv
    click(1100,450)




"""
~~~~~~~~~~PROGRAM START~~~~~~~~~~~~
"""


stime = time.time() + 4800
setup()

#Prif
click(1120,240) #teleport
time.sleep(3)
click(810,330)
time.sleep(30)

#face SOUTH
click2(1110,80)
win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0,0,0)
time.sleep(1)
click(1110,120)
time.sleep(2)

click(1075,150)
time.sleep(12)
click(1075,160)
time.sleep(12)
click(1075,160)
time.sleep(12)
click(1075,160)
time.sleep(12)

click(710,120)

win32api.keybd_event(0x26, 0,0,0)
time.sleep(3)
win32api.keybd_event(0x26,0 ,win32con.KEYEVENTF_KEYUP ,0)
time.sleep(1)
click(1010,380)
"""
click(1110,80)

#Moving
click(1235,250)
time.sleep(15)
click(1320,250)
time.sleep(20)
click(1235,250)
time.sleep(15)
click(1235,250)
time.sleep(15)

click(1020,440)
time.sleep(2)
click(1020,440)
time.sleep(2)    
click(1020,440)
time.sleep(2)
click(1020,440)
time.sleep(5)

click(835,135)
time.sleep(15)

win32api.keybd_event(0x26, 0,0,0)
time.sleep(3)
win32api.keybd_event(0x26,0 ,win32con.KEYEVENTF_KEYUP ,0)

"""
while time.time() < stime:
    #Thing to train goes here
    click(1020,380)
    time.sleep(30)
    print time.time() - stime
"""
    



    
