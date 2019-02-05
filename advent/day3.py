import matplotlib.pyplot as plt
import numpy as np

file = open('claims.txt', 'r')
lines = file.readlines()
claims = []
total = 0

class claim():
    def __init__(self, ID, location, size):
        self.ID = ID
        self.location = location
        self.size = size
        
    

for line in lines:
    info = line.split(' ')
    ID = int(info[0].replace('#', ''))
    coords = info[2].replace(':', '')
    x,y = coords.split(',')
    x = int(x)
    y = int(y)
    size = info[3].replace('\n', '')
    dx, dy = size.split('x')
    dx = int(dx)
    dy = int(dy)
    total += dx*dy
    claims.append(claim(ID, (x,y), (dx,dy)))
    
fabric = [[0]*1000]*1000 #AAAH, REFERENCES
fabric = np.array(fabric) #makes the pointers not fuck up

for claim in claims:
    dx, dy = claim.size
    x,y = claim.location
    for i in range(dx):
        for j in range(dy):
            fabric[x + i][y + j] +=1
            
print("Total = ", total)

overlaps = 0
for strip in fabric:
    for inch in strip:
        if inch >= 2:
            #print('inch = ', inch)
            overlaps += 1
            #print('overlaps = ', overlaps)
            #input()
            
#plt.imshow(fabric)            
#print(overlaps)
            
for claim in claims:
    dx, dy = claim.size
    x,y = claim.location
    overlap = False
    for i in range(dx):
        for j in range(dy):
            if fabric[x + i][y + j] >= 2:
                overlap = True
    if overlap == False:
        print("The chosen claim is ", claim.ID)
        for i in range(dx):
            for j in range(dy):
                fabric[x + i][y + j] = 10
                
plt.imshow(fabric) 
