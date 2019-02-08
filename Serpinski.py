import turtle
import math
import random

"""
l = length of the side of each triangle

r is a number. A random number between 0 and r is chosen, and if it equals 1, 
the turtle will draw the wrong color of triangle

r is incremented by learning after each tier. So, if you want the turtle to
make a mistake, then get better over time for a much more chaotic tringle, 
set r and learning to both not be 0
"""
l=10
r=0
learning=0

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
            else:
                L.append(1)
                t.begin_fill()
        elif m==1:
            if random.randint(0,r)==1:
                L.append(0)
            else:
                L.append(1)
                t.begin_fill()
        elif (L[a-n]==L[a-(n-1)]):
            if random.randint(0,r)==1:
                L.append(1)
                t.begin_fill()
            else:
                L.append(0)
        else:
            if random.randint(0,r)==1:
                L.append(0)
            else:
                L.append(1)
                t.begin_fill()
        t.right(120)
        t.forward(l)
        t.right(120)
        t.forward(l)
        t.right(120)
        t.forward(l)
        t.end_fill()
        m=m-1
        r=r+learning
        
        


