import turtle
import math
import random
import winsound

l=10
r=0
learning=0

p=500
q=1000
d=500

t = turtle.Turtle()
t.shape("turtle")
y=(3**.5)*.5*l
n=0
a=0
L=[1]

t.left(60)
t.penup()
t.sety(250)
t.pendown()

while 1:
    n=n+1
    m=n
    while m>0:
        t.penup()
        t.setx(-.5*l*n+l*(n-m))
        t.sety(250-y*n)
        t.pendown()
        a=a+1
        if m==n:
            if random.randint(0,r)==1:
                L.append(0)
                winsound.Beep(q,d)
            else:
                L.append(1)
                t.begin_fill()
                winsound.Beep(p,d)
        elif m==1:
            if random.randint(0,r)==1:
                L.append(0)
                winsound.Beep(q,d)
            else:
                L.append(1)
                t.begin_fill()
                winsound.Beep(p,d)
        elif (L[a-n]==L[a-(n-1)]):
            if random.randint(0,r)==1:
                L.append(1)
                t.begin_fill()
                winsound.Beep(p,d)
            else:
                L.append(0)
                winsound.Beep(q,d)
        else:
            if random.randint(0,r)==1:
                L.append(0)
                winsound.Beep(q,d)
            else:
                L.append(1)
                t.begin_fill()
                winsound.Beep(p,d)
        t.right(120)
        t.forward(l)
        t.right(120)
        t.forward(l)
        t.right(120)
        t.forward(l)
        t.end_fill()
        m=m-1
        r=r+learning
        
        


