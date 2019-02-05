import win32api, win32con
import time, random, math

#win32api.GetCursorPos()
def click(x,y):
    a,b = win32api.GetCursorPos()
    time.sleep(.1)
    win32api.keybd_event(0xBD  ,0 ,0)
    time.sleep(.1)
    try:
        win32api.SetCursorPos((x,y))
        win32api.keybd_event(0xDB  ,0 ,0) #[
        time.sleep(.5)
        win32api.SetCursorPos((a,b))
        
    except win32api.error:
        print "Error"
        time.sleep(1)
        click(x,y)


def click2(x,y):
    win32api.keybd_event(0xBD  ,0 ,0)
    try:
        win32api.SetCursorPos((x,y))
    except win32api.error:
        print "Errol"
        time.sleep(1)
        win32api.keybd_event(0xDC  ,0 ,0)
        click2(x,y)
        

def click3():
    win32api.keybd_event(0xDC  ,0 ,0)
    win32api.keybd_event(0xDD  ,0 ,0)
    win32api.keybd_event(0xDC  ,0 ,0)
    time.sleep(0) # increase to 10 if there is lots of lag

def test():
    time.sleep(3)
    key_1()
    

def randClick3():
    x,y = win32api.GetCursorPos()
    a = x + random.randint(-3,3)
    b = y + random.randint(-3,3) 
    win32api.SetCursorPos((a,b))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
    win32api.SetCursorPos((x,y))
    time.sleep(0) # increase to 10 if there is lots of lag

def key_enter():
    win32api.keybd_event(0x0D,0 ,0 ,0)

def key_tab():
    win32api.keybd_event(0x09,0 ,0 ,0)

def key_b():
    win32api.keybd_event(0x42,0 ,0 ,0)

def key_i():
    win32api.keybd_event(0x49,0 ,0 ,0)
    
def key_k():
    win32api.keybd_event(0x4B,0 ,0 ,0)

def key_u():
    win32api.keybd_event(0x55,0 ,0 ,0)

def key_y():
    win32api.keybd_event(0x59,0 ,0 ,0)

def key_1():
    win32api.keybd_event(0x31,0 ,0 ,0)

def key_2():
    win32api.keybd_event(0x32,0 ,0 ,0)

def key_3():
    win32api.keybd_event(0x33,0 ,0 ,0)

def key_4():
    win32api.keybd_event(0x34,0 ,0 ,0)

def key_5():
    win32api.keybd_event(0x35,0 ,0 ,0)

def key_6():
    win32api.keybd_event(0x36,0 ,0 ,0)

def key_7():
    win32api.keybd_event(0x37,0 ,0 ,0)

def key_8():
    win32api.keybd_event(0x38,0 ,0 ,0)    

def zoom_out():
    win32api.keybd_event(0x22, 0,0,0)
    time.sleep(3)
    win32api.keybd_event(0x22,0 ,win32con.KEYEVENTF_KEYUP ,0)

def faceSouth():
    time.sleep(.2)
    click2(1305, 92)
    click3()
    time.sleep(1)

    click(1305, 130)

def faceNorth():
    click(1302, 84)

def bank():
    click(1305, 205)
    time.sleep(.5)
    click(1151, 382)
    time.sleep(20)

    click(1898, 380)
    time.sleep(7)
    click(1089, 1016) #1
    time.sleep(.5)
    click(1448, 1019) #2
    time.sleep(.5)
    click(1477, 1023) #3
    time.sleep(.5)
    click(1518, 1023) #4
    time.sleep(.5)

    click(1434, 485)
    time.sleep(.5)
    click(1089, 1016)
    time.sleep(.5)
    click(1555, 1019) #5
    time.sleep(.5)

    click(1434, 485)
    time.sleep(.5)
    click(1089, 1016) 
    time.sleep(.5)
    click(1590, 1017) #6
    time.sleep(.5)

    click(1434, 485)
    time.sleep(.3)
    click(1089, 1016) 
    time.sleep(.3)
    
def bankRC():
    click(1477, 548) #b
    time.sleep(.3)
    click(1089, 1016) #1
    time.sleep(.3)
    click(1448, 1019) #2
    time.sleep(.1)
    click(1477, 1023) #3
    time.sleep(.1)
    click(1518, 1023) #4
    time.sleep(.1)

    click(1477, 548)
    time.sleep(.3)
    click(1089, 1016)
    time.sleep(.3)
    click(1555, 1019) #5
    time.sleep(.1)

    click(1477, 548)
    time.sleep(.3)
    click(1089, 1016)
    time.sleep(.3)
    click(1590, 1017) #6
    time.sleep(.1)

    click(1477, 548)
    time.sleep(.3)
    click(1089, 1016) 
    time.sleep(.3)
    
    
def mudcrafting():
    time.sleep(10)
    win32api.keybd_event(0xDE  ,0 ,0)
    print "ACTIVATE!"
    
    bankRC()
    faceSouth()

    click(1785, 273)
    time.sleep(10)
    click(1640, 243)
    time.sleep(10)
    click(1683, 251)
    time.sleep(12)
    
    click(1769, 688)
    time.sleep(5)
    click(1410, 1019)
    time.sleep(2)
    click(1883, 784)
    time.sleep(1)
    click(1638, 527)
    time.sleep(6)
    click(1098, 495)

    faceNorth()
    time.sleep(12)
    click(1800, 239) #rats??
    time.sleep(10)
    click(1670, 236)
    time.sleep(12)
    click(1487, 523)
    time.sleep(3)

def resetRun():
    win32api.keybd_event(0xC0 ,0 ,0) 
    click(1693, 756)
    time.sleep(1)
    click2(1848, 825)
    click3()
    click(1848, 865)
    time.sleep(8)

    faceSouth()
    click(1335, 289)
    time.sleep(6)
    faceNorth()
    time.sleep(.5)
    click(1651, 747)
    time.sleep(.5)

    #abyss lurker?
    #repair pouches
    #switch massive pouchd
    

def printTime(startTime):
    ftime =  startTime
    hours = int(math.floor(ftime/3600.0))
    mins = int(math.floor((ftime-hours*3600.0)/60.0))
    secs = int(ftime-hours*3600.0-mins*60.0)
    if hours > 0:
        print hours, "hours,",
    if mins > 0:
        print mins, "minutes,",
    print secs,"seconds"

def nats():
    bank()
    
    click(1694, 750)
    time.sleep(1)
    click2(1640, 824)
    click3()
    time.sleep(.2)
    click(1635, 871)
    time.sleep(10)

    click(1432, 736)
    time.sleep(2)
    click(1291, 662)
    time.sleep(2)
    click(1291, 662)
    time.sleep(2)
    click(1291, 662)
    time.sleep(2)
    click(1550, 299)
    time.sleep(10)

    click(1588, 357)
    time.sleep(8)
    
    click(1755, 121)
    time.sleep(15)
    click(1446, 449)
    time.sleep(6)
    click(1438, 358)
    time.sleep(4)
    print "done."


    









    
    
