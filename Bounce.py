import win32api, win32con
import time, random

def click2(x,y):
    win32api.SetCursorPos((x,y))

t = 0
right = 1
down = 1
x = random.randint(0, 1366)
y = random.randint(0, 766)

while t < 5000:
    click2(x,y)
    time.sleep(.005)
    if right == 1 and down == 1:
        x+=1
        y+=1
    if right == 1 and down == -1:
        x+=1
        y-=1
    if right == -1 and down == 1:
        x-=1
        y+=1
    if right == -1 and down == -1:
        x-=1
        y-=1
        
    if x > 1366:
        right = -1
    if x < 0:
        right = 1
    if y > 766:
        down = -1
    if y < 0:
        down = 1
    t+=1
