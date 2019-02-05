import time, math

# 1hr 
#comments? FUN?!

again = 'y'

while again =='y' or again == 'Y':
    try:
        log = open('log.txt','r')  #log = open('log.txt','w') to delete
    except IOError:
        print ("IOError")
        log = open('log.txt','w')
        log.close()
        log = open('log.txt','r')

    prev = log.read()
    n=0
    m=0
    i=0
    j=0
    stime=0
    ftime=0
    ttime=0
    rtime=0
    #goal=prev[0]
    #print goal
    record = []
    record2 = []
    print(prev)

    log.close()


    stime = time.time()

    for item in prev:
        m=0
        i=0
        if prev[n] == '-':
            j=0
        while prev[n+m] != '-' and j==0:
            m+=1
            i=1
        if i==1:
            record2.append(int(prev[n:n+m]))
            j=1
        n+=1
    ptime = 14400 - sum(record2) % 14400
    n=0

    print("\nTime Remaining =", end = "")
    hours4 = int(math.floor(ptime/3600.0))
    mins4 = int(math.floor((ptime-hours4*3600.0)/60.0))
    secs4 = int(ptime-hours4*3600.0-mins4*60.0)
    if hours4 > 0:
        print( hours4, "hours,", end = "")
    if mins4 > 0:
        print( mins4, "minutes,",end = "")
    print( secs4,"seconds")
    

    again = input("Was the time well spent? ")
    if again =='y' or again == 'Y':
        ftime = int(round(time.time() - stime))

        hours = int(math.floor(ftime/3600.0))
        mins = int(math.floor((ftime-hours*3600.0)/60.0))
        secs = int(ftime-hours*3600.0-mins*60.0)
        if hours > 0:
            print( hours, "hours,",end = "")
        if mins > 0:
            print( mins, "minutes,",end = "")
        print( secs,"seconds")



        for item in prev:
            m=0
            i=0
            if prev[n] == '-':
                j=0
            while prev[n+m] != '-' and j==0:
                m+=1
                i=1
            if i==1:
                record.append(int(prev[n:n+m]))
                j=1
            n+=1
        ttime = sum(record) + ftime
        #print sum(record), record
        #print "ttime", ttime
        print( "Total = ",end = "")

        hours2 = int(math.floor(ttime/3600.0))
        mins2 = int(math.floor((ttime-hours2*3600.0)/60.0))
        secs2 = int(ttime-hours2*3600.0-mins2*60.0)
        if hours2 > 0:
            print( hours2, "hours,",end = "")
        if mins2 > 0:
            print( mins2, "minutes,",end = "")
        print( secs2,"seconds")

        rtime = 14400 - (ttime % 14400)

        print( "\nTime Remaining =",end = "")
        hours3 = int(math.floor(rtime/3600.0))
        mins3 = int(math.floor((rtime-hours3*3600.0)/60.0))
        secs3 = int(rtime-hours3*3600.0-mins3*60.0)
        if hours3 > 0:
            print( hours3, "hours,", end = "")
        if mins3 > 0:
            print( mins3, "minutes,",end = "")
        print( secs3,"seconds")



        if ((ttime -ftime)% 14400) > ((ttime)% 14400):
            print( "\nCongratulations! You have earned a character an extra life!")
            #goal+=1
            
        log = open('log.txt','w')
        log.write(prev)
        log.write(str(ftime))
        log.write("-")
        log.close()

        again = input("Again?")
        if again == 'y' or again == 'Y':
            print ('\n\n\n')

            #What is even the point of this?!? (Just an again??)
            
  
    else:
        #log.write(prev)
        again = input("Again?")

