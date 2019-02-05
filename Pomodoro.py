import winsound
import time
"""
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
s = 5 *60
l = 30*60
p = 3-1

b=0
x=0

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
    winsound.Beep(int(e4),200)
    winsound.Beep(int(E4),200)
    winsound.Beep(int(F4),200)
    winsound.Beep(int(g4),1000)
    
def long():
    winsound.Beep(int(A4),300)
    winsound.Beep(int(A4),100)
    winsound.Beep(int(A4),100)
    winsound.Beep(int(G4),100)
    winsound.Beep(int(A4),1000)

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


while 1:
    t=w


 

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
