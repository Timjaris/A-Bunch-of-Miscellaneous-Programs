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

def bank():
    #teleport (use keyboard?)
    click(1120,240)
    time.sleep(3)
    click(790,230)
    time.sleep(30)

    #bank
    click(1290,140)
    time.sleep(9)
    click(1075,350)
    time.sleep(3)
    click(810,700)
    time.sleep(2)

def portphas():
    #Port Phasmatys
    click(1170,480) #Moving
    time.sleep(12)
    click(1120,105)
    time.sleep(15)
    click(985,220)
    time.sleep(6)
    click(1025,350)
    time.sleep(6)
    click(950,450)
    time.sleep(6)
    click(950,450)
    time.sleep(6)
    click(720,400)
    time.sleep(6)
    click(720,400)
    time.sleep(6)
    click(930,600)
    time.sleep(6)
    click(1024,440)
    time.sleep(6)

    click(990,410) #Farming
    time.sleep(30)
    click(1250,480)
    time.sleep(1)
    click(1010,400)
    time.sleep(3)
    click(1090,480)
    time.sleep(1)
    click(1010,400)
    time.sleep(3)


def cabbages():
    #Cabbages
    click(1140,440) #teleporting
    time.sleep(1)
    click2(1165,520) #Yes, 2
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0,0,0)
    time.sleep(1)
    click(1140,570)
    time.sleep(8)

    click(1260,88) #Moving
    time.sleep(25)
    click(1070,380)
    time.sleep(3)
    click(1050,350) #Farming
    time.sleep(30)
    click(1100,450)
    time.sleep(1)
    click(1250,480)
    time.sleep(1)
    click(1050,350)
    time.sleep(3)
    click(1090,480)
    time.sleep(1)
    click(1050,350)
    time.sleep(3)

def cathers():
    #Cathers
    click(1120,240) #teleport
    time.sleep(3)
    click(955,330)
    time.sleep(30)

    click(700,225) #moving
    time.sleep(10)
    click(850,260)
    time.sleep(10)

    click(1000,420)
    time.sleep(20)
    click(1100,450)
    time.sleep(1)
    click(1250,480)
    time.sleep(1)
    click(1000,420)
    time.sleep(3)
    click(1090,480)
    time.sleep(1)
    click(1000,420)
    time.sleep(3)

def ard():
    #Ard
    click(1120,240) #teleport
    time.sleep(3)
    click(915,335)
    time.sleep(30)

    click(1350,116) #Moving
    time.sleep(25)
    click(850,450)
    time.sleep(6)
    click(850,450)
    time.sleep(8)
    click(1285,96)
    time.sleep(15)

    click(1000,420) #farming
    time.sleep(30)
    click(1100,450)
    time.sleep(1)
    click(1250,480)
    time.sleep(1)
    click(1000,420)
    time.sleep(3)
    click(1090,480)
    time.sleep(1)
    click(1000,420)
    time.sleep(3)

def priffy():
    #Prif
    click(1120,240) #teleport
    time.sleep(3)
    click(810,330)
    time.sleep(30)

    #face north
    click(1110,80)

    click(1360,114) #moving
    time.sleep(30)
    click(1300,90)
    time.sleep(16)
    click(1055,420)
    time.sleep(3)

    click(1000,420) #farming?
    time.sleep(30)
    click(1100,450)
    time.sleep(1)
    click(1250,480)
    time.sleep(1)
    click(1000,420)
    time.sleep(3)
    click(1090,480)
    time.sleep(1)
    click(1000,420)
    time.sleep(3)


def troll():
    #Troll
    click(1220,450) #teleport
    time.sleep(1)
    click(1140,470)
    time.sleep(1)
    click(1150,550)
    time.sleep(20)

    click(1110,80) #north

    click(1120,120) #moving
    time.sleep(35)
    click(1020,360)
    time.sleep(8)
    click(1020,360)
    time.sleep(4)
    click(1020,360)
    time.sleep(3)
    click(1020,360)
    time.sleep(2)
    click(1020,360)
    time.sleep(2)
    click(1020,360)
    time.sleep(2)
    click(910,120)
    time.sleep(20)

    click(1212,215) #moving in cave
    time.sleep(25)
    click(1020,340)
    time.sleep(7)

    click(1080,130) #farming
    time.sleep(35)
    click(1100,450)
    time.sleep(1)
    click(1250,480)
    time.sleep(1)
    click(1080,350)
    time.sleep(4)
    click(1090,480)
    time.sleep(1)
    click(1080,350)
    
def cathers2():
    #Cathers
    click(1120,240) #teleport
    time.sleep(3)
    click(955,330)
    time.sleep(30)

    click(1300,250)
    time.sleep(20)
    click(1310,175)
    time.sleep(10)
    click(850,230)
    time.sleep(15)

def gnomestr():
    click(1220,450) #teleport
    time.sleep(1)
    click(1140,470)
    time.sleep(1)
    click(1120,500)
    time.sleep(10)
    
    click2(1300,300)
    time.sleep(1)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0,0,0)
    time.sleep(1)
    click(1300,340)
    time.sleep(8)
    win32api.keybd_event(0x32, 0,0,0)
    time.sleep(8)
    click(1350,380)
    time.sleep(5)
    click(1350,380)
    time.sleep(5)
    click(1100,385)
    time.sleep(10)

def gnomevil():
    click(1120,240) #teleport
    time.sleep(3)
    click(810,330)
    time.sleep(30)

    #face north
    click(1110,80)

    #gnome glider
    click(1235,80)
    time.sleep(10)
    click(1235,80)
    time.sleep(10)
    click(1235,80)
    time.sleep(10)
    click(1235,80)
    time.sleep(10)
    click(1235,100)
    time.sleep(10)
    click(1110,395)
    time.sleep(2)
    click(1110,395)
    time.sleep(2)
    click(1110,395)
    time.sleep(2)
    
    click2(900,420)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0,0,0)
    time.sleep(1)
    click(900,460)
    time.sleep(15)
    click(1020,340)
    time.sleep(5)
    win32api.keybd_event(0x37, 0,0,0)
    time.sleep(10)

    click(920,630)
    time.sleep(6)
    click(920,630)
    time.sleep(6)
    click(920,480)
    time.sleep(10)

def lletya():
    click(1140,440) #teleporting
    time.sleep(1)
    click2(1215,520) #Yes, 2
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0,0,0)
    time.sleep(1)
    click(1140,570)
    time.sleep(1)
    click(1115,420)
    time.sleep(8)

    click(1295,250)
    time.sleep(10)
    click(1010,430)
    time.sleep(2)
    click(1010,430)
    time.sleep(2)
    click(1010,430)
    time.sleep(2)
    click(1010,430)
    time.sleep(2)
    click(1010,430)
    time.sleep(2)
    click(1010,430)
    time.sleep(2)
    click(1010,330)
    time.sleep(8)
    click(840,120)
    time.sleep(20)

def brimh():
    #FUCK IT, USE SPIRIT TREE
    """
    click(1120,240)
    time.sleep(3)
    click(950,390)
    time.sleep(30)

    click(1235,80)
    time.sleep(10)
    click(1235,80)
    time.sleep(10)
    click(1235,80)
    time.sleep(10)
    click(1030,300)
    """

def herbhab():
    #GET WITCHDOCTOR MASK
    no = 1


"""
~~~~~~~~~~PROGRAM START~~~~~~~~~~~~
"""
while 1:
    stime = time.time() #+ 4800
    setup()

    #Prif
    click(1120,240) #teleport
    time.sleep(3)
    click(810,330)
    time.sleep(30)

    #face north
    click(1110,80)
    
    while time.time() < stime:
        #Thing to train goes here
        print "lol"
        

    setup()

    bank()

    portphas()

    bank()

    cabbages()

    bank()

    cathers()

    bank()

    ard()

    bank()

    priffy()

    bank()

    troll()

    if 1:
        bank()
        
        cathers2()
        
        gnomestr()

        bank()
        
        gnomevil()
        
        lletya()
        """
        bank()
        
        brimh()

        herbhab()

        bank()
        
        priffy2()
        """
        x = 1
    else:
        x = 0



    
