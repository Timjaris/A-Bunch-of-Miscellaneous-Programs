import winsound, time, math
"""
54000-1343-160-460-3097-1463-1193-3215-760-1996-2958-518-3810-213-509-423-1303-1-468-1615-912-4788-1653-7555-863-2821-7385-7252-2351-1660-1823-589-1273-625-3691-528-2172-2760-1866-398-2009-887-3462-254-3778-4151-
print("In minutes:")
w=input("Work Period=")
w=int(w)*60
s=input("Short Break=")
s=int(s)*60
l=input("Long Break=")
l=int(l)*60
p=int(input("Number of Work Periods per Cycle="))
p=p-1
"""

w = 25*60
s = 10 *60
l = 60*60
p = 2-1
b=0
x=0

worktime = 0
again = 'y'
n1=0
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

n=-29

E2=440*((2**(.08333))**n)
n=n+1
F2=440*((2**(.08333))**n)
n=n+1
g2=440*((2**(.08333))**n)
n=n+1
G2=440*((2**(.08333))**n)
n=n+1
a2=440*((2**(.08333))**n)
n=n+1
A2=440*((2**(.08333))**n)
n=n+1
b2=440*((2**(.08333))**n)
n=n+1
B2=440*((2**(.08333))**n)
n=n+1
C3=440*((2**(.08333))**n)
n=n+1
d3=440*((2**(.08333))**n)
n=n+1
D3=440*((2**(.08333))**n)
n=n+1
e3=440*((2**(.08333))**n)
n=n+1
E3=440*((2**(.08333))**n)
n=n+1
F3=440*((2**(.08333))**n)
n=n+1
g3=440*((2**(.08333))**n)
n=n+1
G3=440*((2**(.08333))**n)
n=n+1
a3=440*((2**(.08333))**n)
n=n+1
A3=440*((2**(.08333))**n)
n=n+1
b3=440*((2**(.08333))**n)
n=n+1
B3=440*((2**(.08333))**n)
n=n+1
C4=440*((2**(.08333))**n)
n=n+1
d4=440*((2**(.08333))**n)
n=n+1
D4=440*((2**(.08333))**n)
n=n+1
e4=440*((2**(.08333))**n)
n=n+1
E4=440*((2**(.08333))**n)
n=n+1
F4=440*((2**(.08333))**n)
n=n+1
g4=440*((2**(.08333))**n)
n=n+1
G4=440*((2**(.08333))**n)
n=n+1
a4=440*((2**(.08333))**n)
n=n+1
A4=440
n=n+1
b4=440*((2**(.08333))**n)
n=n+1
B4=440*((2**(.08333))**n)
n=n+1
C5=440*((2**(.08333))**n)
n=n+1
d5=440*((2**(.08333))**n)
n=n+1
D5=440*((2**(.08333))**n)
n=n+1
e5=440*((2**(.08333))**n)
n=n+1
E5=440*((2**(.08333))**n)
n=n+1
F5=440*((2**(.08333))**n)
n=n+1
g5=440*((2**(.08333))**n)
n=n+1
G5=440*((2**(.08333))**n)
n=n+1
a5=440*((2**(.08333))**n)
n=n+1
A5=440*((2**(.08333))**n)
n=n+1
b5=440*((2**(.08333))**n)
n=n+1
B5=440*((2**(.08333))**n)
n=n+1
C6=440*((2**(.08333))**n)

def short():
    winsound.Beep(int(e4),300)
    winsound.Beep(int(E4),300)
    winsound.Beep(int(F4),300)
    winsound.Beep(int(g4),1500)
    
def long():
    winsound.Beep(int(A4),450)
    winsound.Beep(int(A4),150)
    winsound.Beep(int(A4),150)
    winsound.Beep(int(G4),150)
    winsound.Beep(int(A4),1500)

def work():
    winsound.Beep(int(A3),500)
    winsound.Beep(int(D3),1000)
    winsound.Beep(int(F3),500)
    winsound.Beep(int(A3),500)
    winsound.Beep(int(D3),1000)
    winsound.Beep(int(F3),500)
    winsound.Beep(int(A3),250)
    winsound.Beep(int(C4),250)
    winsound.Beep(int(B3),500)
    winsound.Beep(int(G3),500)
    winsound.Beep(int(F3),250)
    winsound.Beep(int(g3),250)
    winsound.Beep(int(A3),500)
    winsound.Beep(int(D3),500)
    winsound.Beep(int(C3),250)
    winsound.Beep(int(E3),250)
    winsound.Beep(int(D3),2000)

t=2*l
while t != 0:
    print("Long Break")
    print (int(t/60), "minutes",t%60, 'Seconds')
    print(" ")
    time.sleep(.99)
    t=t-1
work()

while 1:
    t=w
    n1=0
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
    while t != 0:
        print("Work Time", b+1, "out of", p+1)
        print (int(t/60), "minutes",t%60, 'Seconds left')
        print(" ")
        time.sleep(.99)
        t=t-1

    if b!=p:
        b=b+1
        t=s
        short()
        x=0
    else:
        b=0
        t=l
        long()
        x=1
        
    again = raw_input("Was the time well spent? ")
    if again == 'y' or again == 'Y':
        ftime = w

        hours = int(math.floor(ftime/3600.0))
        mins = int(math.floor((ftime-hours*3600.0)/60.0))
        secs = int(ftime-hours*3600.0-mins*60.0)
        if hours > 0:
            print hours, "hours,",
        if mins > 0:
            print mins, "minutes,",
        print secs,"seconds"
        
        try:
            log = open('log.txt','r')  #log = open('log.txt','w') to delete
        except IOError:
            print "IOError"
            log = open('log.txt','w')
            log.close()
            log = open('log.txt','r')
        prev = log.read()
        log.close()
        for item in prev:
            m=0
            i=0
            if prev[n1] == '-':
                j=0
            while prev[n1+m] != '-' and j==0:
                m+=1
                i=1
            if i==1:
                record.append(int(prev[n1:n1+m]))
                j=1
            n1+=1
        ttime = sum(record) + ftime

        hours2 = int(math.floor(ttime/3600.0))
        mins2 = int(math.floor((ttime-hours2*3600.0)/60.0))
        secs2 = int(ttime-hours2*3600.0-mins2*60.0)
        print "Total = ",
        if hours2 > 0:
            print hours2, "hours,",
        if mins2 > 0:
            print mins2, "minutes,",
        print secs2,"seconds"

        rtime = 14400 - (ttime % 14400)

        print "\nTime Remaining =",
        hours3 = int(math.floor(rtime/3600.0))
        mins3 = int(math.floor((rtime-hours3*3600.0)/60.0))
        secs3 = int(rtime-hours3*3600.0-mins3*60.0)
        if hours3 > 0:
            print hours3, "hours,",
        if mins3 > 0:
            print mins3, "minutes,",
        print secs3,"seconds"

        if ((ttime -ftime)% 14400) > ((ttime)% 14400):
            print "\nCongratulations! You have earned a character an extra life!"
 
        log = open('log.txt','w')
        log.write(prev)
        log.write(str(ftime))
        log.write("-")
        log.close()
    


 
    while t != 0:
        if x==0:
            print("Short Break", b, "out of", p)
        if x==1:
            print("Long Break")
        print (int(t/60), "minutes",t%60, 'Seconds')
        print(" ")
        time.sleep(.99)
        t=t-1
    work()
