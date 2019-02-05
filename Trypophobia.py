import time as t, math, winsound

def chorus(s, t):
    c=2*261.63
    d=2*293.66
    e=2*329.63
    f=2*349.23
    g=2*392
    A=2*440
    B=2*493.88
    C=2*523.25
    D=2*587.33
    E=2*659.25
    F=2*698.46
    G=2*783.99 
    import time
    winsound.Beep(int(s*A),int(t))
    time.sleep(.01)
    winsound.Beep(int(s*d),int(2*t))
    time.sleep(.01)
    winsound.Beep(int(s*f),int(t))
    time.sleep(.01)
    winsound.Beep(int(s*A),int(t))
    time.sleep(.01)
    winsound.Beep(int(s*d),int(2*t))
    time.sleep(.01)
    winsound.Beep(int(s*f),int(t))
    time.sleep(.01)
    winsound.Beep(int(s*A),int(t/2))
    time.sleep(.01)
    winsound.Beep(int(s*C),int(t/2))
    time.sleep(.01)
    winsound.Beep(int(s*B),int(t))
    time.sleep(.01)
    winsound.Beep(int(s*g),int(t))
    time.sleep(.01)
    winsound.Beep(int(s*f),int(.5*t))
    time.sleep(.01)
    winsound.Beep(int(s*g),int(.5*t))
    time.sleep(.01)
    winsound.Beep(int(s*A),int(t))
    time.sleep(.01)
    winsound.Beep(int(s*d),int(t))
    time.sleep(.01)
    winsound.Beep(int(s*c),int(.5*t))
    time.sleep(.01)
    winsound.Beep(int(s*e),int(.5*t))
    time.sleep(.01)

def printTime(time):
    hours = int(math.floor(time/3600.0))
    mins = int(math.floor((time-hours*3600.0)/60.0))
    secs = int(time-hours*3600.0-mins*60.0)
    if hours > 0:
        print(hours, "hours,", end = '')
    if mins > 0:
        print(mins, "minutes,", end = '')
    print(secs,"seconds")

def getTotalTime():
    try:
        log = open('log.txt','r')  #log = open('log.txt','w') to delete
    except IOError:
        print("IOError")
        log = open('log.txt','w')
        log.close()
        log = open('log.txt','r')
    prev = log.read()
    log.close()
    total = 0
    for item in prev.split('-')[0:len(prev.split('-'))-1]: #lol
        total += int(item)
    
    return total

def writeNewTime(time):
    log = open('log.txt', 'a')
    log.write(str(time) + '-')
    log.close()

def recess(time):
    for i in range(time):
        rem = time-i
        t.sleep(1)
        print("Break time remaining: ", end = '')
        printTime(rem)
    chorus(.5, 500)


        
def check(ftime, rtime):
    if ftime > rtime:
        print("Congratulations! You have earned a character an extra life!")
        print("Time remaining: ", 14400 + rtime - ftime)
    else:
        print("Time remaining: ", rtime - ftime)
    
while(1):
    breakTime = 15*60
    total = getTotalTime()
    rtime =  14400 - (total % 14400)
    print("Time remaining: ", end = '')
    printTime(rtime)
    stime = t.time()
    input("Break? ")
    ftime = round(t.time() - stime)
    printTime(ftime)
    writeNewTime(ftime)
    recess(breakTime)
    





def songOfTime():
    t=500
    s = .5
    
    c=2*261.63
    d=2*293.66
    e=2*329.63
    f=2*349.23
    g=2*392
    A=2*440
    B=2*493.88
    C=2*523.25
    D=2*587.33
    E=2*659.25
    F=2*698.46
    G=2*783.99    
    
    main(s, t)
    winsound.Beep(int(s*d),int(t))
    main(s, t)
    
    winsound.Beep(int(s*d),int(5*t))
    
    winsound.Beep(int(s*d),int(t/2))
    winsound.Beep(int(s*c),int(t/2))
    winsound.Beep(int(s*e),int(t))
    winsound.Beep(int(s*c),int(t))
    winsound.Beep(int(s*e),int(t/2))
    winsound.Beep(int(s*f),int(t/2))
    winsound.Beep(int(s*d),int(t*4))
    
    winsound.Beep(int(s*d),int(t/2))
    winsound.Beep(int(s*c),int(t/2))
    winsound.Beep(int(s*e),int(t))
    winsound.Beep(int(s*c),int(t))
    winsound.Beep(int(s*f),int(t/2))
    winsound.Beep(int(s*g),int(t/2))
    winsound.Beep(int(s*d),int(4*t))
    
    winsound.Beep(int(s*A),int(.5*t))
    winsound.Beep(int(s*C),int(.5*t))
    winsound.Beep(int(s*B),int(t))
    winsound.Beep(int(s*C),int(t))
    winsound.Beep(int(s*A),int(t))
    winsound.Beep(int(s*C),int(t))
    winsound.Beep(int(s*g),int(t))
    winsound.Beep(int(s*A),int(t))
    winsound.Beep(int(s*d),int(.5*t))
    winsound.Beep(int(s*c),int(.5*t))
    winsound.Beep(int(s*e),int(t))
    winsound.Beep(int(s*d),int(t*3))
    
    winsound.Beep(int(s*f),int(t/2))
    winsound.Beep(int(s*g),int(t/2))
    winsound.Beep(int(s*f),int(t))
    winsound.Beep(int(s*g),int(t))
    winsound.Beep(int(s*e),int(t/2))
    winsound.Beep(int(s*c),int(t/2))
    winsound.Beep(int(s*f),int(t))
    winsound.Beep(int(s*e),int(t))
    winsound.Beep(int(s*d),int(t*6))
