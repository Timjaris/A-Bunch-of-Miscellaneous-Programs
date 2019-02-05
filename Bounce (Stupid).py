import win32api, win32con
import time, random

def click2(x,y):
    win32api.SetCursorPos((x,y))

t = 0
right = 1
up = 1
x = random.randint(0, 1366)
y = random.randint(0, 766)
click2(x,y)
while t < 1000:
    
    t+=1
