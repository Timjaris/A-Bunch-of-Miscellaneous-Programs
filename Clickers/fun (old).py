import win32api, win32con
import time, random

#Woodcutting
#daily runecrafting?
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

def click3():
    a,b = win32api.GetCursorPos()
    win32api.SetCursorPos((a,b))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
    time.sleep(0) # increase to 10 if there is lots of lag

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
    click(1100,440)

def bank():
    #teleport (use keyboard?)
    click(1120,240)
    time.sleep(3)
    click(790,230)
    time.sleep(30)

    #bank
    click(1284,140)
    time.sleep(9)
    click(1075,350)
    time.sleep(3)
    click(810,690)
    time.sleep(3)

def bank_dep():
    #teleport (use keyboard?)
    click(1120,240)
    time.sleep(3)
    click(790,230)
    time.sleep(30)

    #bank
    click(1284,140)
    time.sleep(9)
    click(1075,350)
    time.sleep(3)
    click(1054, 690)
    time.sleep(1)
    click(1155, 51)
    time.sleep(1)

def portphas():
    #Port Phasmatys
        #Moving
    click(1170,470) #ectofil
    time.sleep(20)
    click(1120,105)
    time.sleep(20)
    click(985,220)
    time.sleep(7)
    click(1025,350)
    time.sleep(7)
    click(853, 693)
    time.sleep(7)
    click(730, 382)
    time.sleep(7)
    click(730, 382)
    time.sleep(6)
    click(875, 482)
    time.sleep(6)
    
    """
    time.sleep(6)
    click(950,450)
    time.sleep(6)
    click(950,450)
    time.sleep(6)
    click(720,390)
    time.sleep(6)
    click(720,390)
    time.sleep(6)
    click(930,600)
    time.sleep(6)
    click(1000,390)
    time.sleep(6)
    """
    click(990,410) #Farming
    time.sleep(30)
    click(1250,480)
    time.sleep(1)
    click(1010,390)
    time.sleep(3)
    click(1090,480)
    time.sleep(1)
    click(1010,390)
    time.sleep(3)
    

def cabbages():
    #Cabbages
    click(1140,440) #teleporting
    time.sleep(1)
    click2(1165,510) #Yes, 2
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0,0,0)
    time.sleep(1)
    click(1140,560)
    time.sleep(20)

    click(1260,88) #Moving
    time.sleep(25)
    click(1070,380)
    time.sleep(3)
    
    click(1050,350) #Farming
    time.sleep(30)
    click(1100,440)  #Inv
    time.sleep(1)
    click(1250,470)
    time.sleep(1)
    click(1050,350)
    time.sleep(3)
    click(1090,470)
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
    click(1100,440)  #inv
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
    click(1282,97) #this fucker
    time.sleep(15)

    click(1000,420) #farming
    time.sleep(30)
    click(1100,440)   #inv
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

    click(1360,114) #moving
    time.sleep(30)
    click(1260,90)
    time.sleep(16)
    click(1050,420)
    time.sleep(3)

    click(1000,420) #farming?
    time.sleep(30)
    click(1100,440)   #inv
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
    #Get livid farm spell
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
    click(1100,440)   #inv
    time.sleep(1)
    click(1250,480)
    time.sleep(1)
    click(1080,350)
    time.sleep(4)
    click(1090,480)
    time.sleep(2)
    click(1080,350)
    time.sleep(2)
    
def cathers2():
    #Cathers
    click(1120,240) #teleport
    time.sleep(3)
    click(955,330)
    time.sleep(30)

    click(1300,250)
    time.sleep(20)
    click(1310,175)
    time.sleep(15)
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
    print "Menu??"
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
    click(1235,100)
    time.sleep(10)
    click(1235,100)
    time.sleep(10)
    click(1100,395)  #???
    time.sleep(2)
    click(1100,395)
    time.sleep(2)
    click(1100,395)
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
    
    click(1140,570)
    time.sleep(4)
    click(1115,420)
    time.sleep(12)

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

def farming():
    a = 1
    
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

    if a == 1:
        a = 0
        
        bank()

        cathers2()
    
        gnomestr()

        bank()

        gnomevil()

        lletya()


def mining(t):
    stime = time.time() + t
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
    time.sleep(18)
    click(1075,160)
    time.sleep(12)
    click(1075,160)
    time.sleep(12)
    click(1075,160)
    time.sleep(12)

    click(710,120)
    time.sleep(1)
    win32api.keybd_event(0x26, 0,0,0)
    time.sleep(3)
    win32api.keybd_event(0x26,0 ,win32con.KEYEVENTF_KEYUP ,0)
    time.sleep(30)

    while time.time() < stime:
        #Thing to train goes here
        click(1020,380)
        time.sleep(30)
        print 4800 - time.time() + stime

def herb():
    click(1155,60)
    time.sleep(1)
    click(850,690)
    time.sleep(2)
    click(850,690)
    win32api.keybd_event(0x20, 0,0,0) #space
    time.sleep(.1)
    win32api.keybd_event(0x20,0 ,win32con.KEYEVENTF_KEYUP ,0)
    

    click(980,690)
    time.sleep(2)
    click(1115, 499)
    time.sleep(18)

def yanille():
    click(1120,240) #teleport
    time.sleep(3)
    click(900,400)
    time.sleep(30)
    
    #face SOUTH
    click2(1110,80)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0,0,0)
    time.sleep(1)
    click(1110,120)
    time.sleep(3)

    click(950,100)
    time.sleep(15)
    click(700,250)
    time.sleep(15)
    click(699, 410)
    time.sleep(15)
    click(699, 410)
    time.sleep(15)
    click(699, 410)
    time.sleep(15)
    click(920, 79)
    time.sleep(150)
    click(970, 175)
    time.sleep(150)
    
    """
    click(833, 116)
    time.sleep(150)
    click(960, 154)
    time.sleep(150)
    """
    
def cabbagetrees():
    #Cabbages
    click(1140,440) #teleporting
    time.sleep(1)
    click2(1165,510) #Yes, 2
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0,0,0)
    time.sleep(1)
    click(1140,560)
    time.sleep(20)

    click(1110,80) #face north
    time.sleep(1)
    click(1260,88) #Moving
    time.sleep(25)
    click(1070,380)
    time.sleep(3)

    click(997, 164) #Woodcutting
    time.sleep(150)
    click(1033, 223)
    time.sleep(150)
    
def varrock():
    click(1120,240) #teleport
    time.sleep(3)
    click(1096, 314)
    time.sleep(20)

    click(1110,80) #face north
    time.sleep(1)
    
    click(1353, 301) #moving
    time.sleep(10)
    click(1355, 365)
    time.sleep(10)
    click(1355, 365)
    time.sleep(10)
    click(1355, 365)
    time.sleep(1)

    #face SOUTH
    click2(1110,80)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0,0,0)
    time.sleep(1)
    click(1110,120)
    time.sleep(3)

    #moving2
    click(734, 276)
    time.sleep(8)
    click(700, 236) #chopin wood
    time.sleep(150)
    click(983, 247)
    time.sleep(150)

    click(1110,80) #face north
    time.sleep(1)
    
    
def openrs():
    #opening rs
    click(9999,9999)
    time.sleep(2)

    win32api.SetCursorPos((40,650))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,40,650,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,40,650,0,0) #make manual double click
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,40,650,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,40,650,0,0)
    time.sleep(20) 
    
    #moving rs to side
    
    win32api.SetCursorPos((750,20))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,750,20,0,0)
    win32api.SetCursorPos((9999,220))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,9999,220,0,0)
    time.sleep(3)
    

    #moving icon to right (assuming it starts at 6th spot)
    win32api.SetCursorPos((380,750))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,380,750,0,0)
    win32api.SetCursorPos((210,750))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,210,750,0,0)
    time.sleep(60) #wait for it to open
    
    #select rs
    click(100,750)
    time.sleep(1)
    click(220,750)
    time.sleep(3)

    key_k()
    time.sleep(.1)
    key_y()
    time.sleep(.1)
    key_u()
    time.sleep(.1)
    key_b()
    time.sleep(.1)
    key_i()
    time.sleep(1)
    key_enter()
    time.sleep(15)

    click(1100,550)
    time.sleep(20)



def closers():
    click(1350,20)
    time.sleep(2)
    key_tab()
    time.sleep(1)
    key_enter()



    
    




