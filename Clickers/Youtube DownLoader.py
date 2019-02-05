import win32api, win32con
import time

def click(x,y):
    a,b = win32api.GetCursorPos()
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

def click2(x,y):
    win32api.SetCursorPos((x,y))

def doubleClick(x,y):
    click(x, y)
    time.sleep(.1)
    click(x, y)

def copy():
    time.sleep(2)
    win32api.keybd_event(0x11,0 ,0 ,0)
    win32api.keybd_event(0x43,0 ,0 ,0)
    win32api.keybd_event(0x11,0 ,win32con.KEYEVENTF_KEYUP ,0)
    time.sleep(2)

def paste():
    time.sleep(1)
    win32api.keybd_event(0x11,0 ,0 ,0)
    win32api.keybd_event(0x56,0 ,0 ,0)
    win32api.keybd_event(0x11,0 ,win32con.KEYEVENTF_KEYUP ,0)
    time.sleep(1)

def selectAll():
    time.sleep(1)
    win32api.keybd_event(0x11,0 ,0 ,0)
    win32api.keybd_event(0x41,0 ,0 ,0)
    win32api.keybd_event(0x11,0 ,win32con.KEYEVENTF_KEYUP ,0)
    time.sleep(1)

def ctrlJ():
    time.sleep(1)
    win32api.keybd_event(0x11,0 ,0 ,0)
    win32api.keybd_event(0x4A,0 ,0 ,0)
    win32api.keybd_event(0x11,0 ,win32con.KEYEVENTF_KEYUP ,0)
    time.sleep(1)

def save():
    time.sleep(1)
    win32api.keybd_event(0x11,0 ,0 ,0)
    win32api.keybd_event(0x53,0 ,0 ,0)
    win32api.keybd_event(0x11,0 ,win32con.KEYEVENTF_KEYUP ,0)
    time.sleep(1)

def close():
    time.sleep(1)
    win32api.keybd_event(0x11,0 ,0 ,0)
    win32api.keybd_event(0x57,0 ,0 ,0)
    win32api.keybd_event(0x11,0 ,win32con.KEYEVENTF_KEYUP ,0)
    time.sleep(1)
    
def enter():
    win32api.keybd_event(0x0D,0 ,0 ,0)
    time.sleep(2)

def getName():
    time.sleep(1)
    win32api.SetCursorPos((976, 548))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0,0)
    click2(1560, 548)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0,0,0)
    copy()

#Main Program
#Get youtube url
time.sleep(5)
while 1:
    click(1311, 97)
    time.sleep(1)
    click(1462, 61)
    copy()
    time.sleep(2)

    #paste to vlc
    click(130, 223)
    paste();
    enter()
    ctrlJ()

    #get video location
    time.sleep(8) #wait for location to load
    click(889, 988)
    selectAll()
    copy()

    click(1311, 97)
    time.sleep(1)
    click(1462, 61)
    paste()
    getName()
    time.sleep(.5)
    click(1462, 61)
    time.sleep(.5)
    enter()

    #Get video
    click(1756, 399)
    time.sleep(1)
    save()
    time.sleep(1)
    paste()
    time.sleep(1)
    enter()
    raw_input("Name? ") #if the title is invalid
    raw_input("Check")
    time.sleep(1)
    close()
    time.sleep(1)

print("Done!")
input()





