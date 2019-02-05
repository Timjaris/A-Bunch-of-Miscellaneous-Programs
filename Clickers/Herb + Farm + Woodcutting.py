import win32api, win32con
import time, fun



n = 0
herbNo = 7900 
while n <  herbNo/26:

    fun.herb()
    n+=1


fun.bank()
while 1:
    fun.farming()

    t = 4800

    fun.mining(t)

    fun.closers()
    fun.openrs()
    

    
