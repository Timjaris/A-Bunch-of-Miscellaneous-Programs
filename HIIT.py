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


w = 15*60
s = 5*60
l = 30*60
p = 3-1
b=0

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

t = 1
def short():
    winsound.Beep(int(e4), 200 // t)
    winsound.Beep(int(E4), 200 // t)
    winsound.Beep(int(F4), 200 // t)
    winsound.Beep(int(g4), 1000 // t)
    
def long():
    winsound.Beep(int(A4), 300 // t)
    winsound.Beep(int(A4), 100 // t)
    winsound.Beep(int(A4), 100 // t)
    winsound.Beep(int(G4), 100 // t)
    winsound.Beep(int(A4), 1000 // t)

def work():
    winsound.Beep(int(A3), 500 // t)
    winsound.Beep(int(D3), 1000 // t)
    winsound.Beep(int(F3), 500 // t)
    winsound.Beep(int(A3), 500 // t)
    winsound.Beep(int(D3), 1000 // t)
    winsound.Beep(int(F3), 500 // t)
    winsound.Beep(int(A3), 250 // t)
    winsound.Beep(int(C4), 250 // t)
    winsound.Beep(int(B3), 500 // t)
    winsound.Beep(int(G3), 500 // t)
    winsound.Beep(int(F3), 250 // t)
    winsound.Beep(int(g3), 250 // t)
    winsound.Beep(int(A3), 500 // t)
    winsound.Beep(int(D3), 500 // t)
    winsound.Beep(int(C3), 250 // t)
    winsound.Beep(int(E3), 250 // t)
    winsound.Beep(int(D3), 2000 // t)

for i in range(10):
    print(i, " / 10")
    brake = 60
    wrk = 30
    work()
    print("Work")
    while wrk:
        wrk -= 1
        time.sleep(1)
    short()
    print("Break")
    while brake:
        brake -= 1
        time.sleep(1)
long()
