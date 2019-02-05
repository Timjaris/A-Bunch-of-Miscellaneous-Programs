# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 16:10:37 2019

@author: Tim
"""
#file = open("inputs.txt", "w")
import string
letters = list(string.ascii_uppercase)
T = int(input())
#file.write(str(T) + "\n")
outputs = []
for i in range(T):
    parties = int(input())
    #file.write(str(parties) + "\n")
    temp = input().split(' ')
    #file.write(str(temp) + "\n")
    dist= []
    for j in range(len(temp)):
        dist.append(int(temp[j]))
    assert parties == len(dist) 
        
    #get first 2 non-zero parties
    rearguard = [None, None]
    uhh = 0
    pos = 0
    #I think this will work with any non-zero party, but if not, change to account for size
    while uhh != 2:
        if dist[pos] != 0: 
            rearguard[uhh] = pos
            uhh += 1
        pos += 1
            
    #Slowest possible evacuation
    output = ""
    while sum(dist) > 2:
        biggest = dist.index(max(dist))
        while biggest in rearguard and dist[biggest] == 1:
            biggest = dist.index(max(dist), biggest+1)
        output += letters[biggest] + " "
        dist[biggest] -= 1
    #super-ineligant patch
    pivot = len(output)-3
    if pivot > 0:
        output = output[:pivot] + output[pivot+1:]
    
    output += letters[rearguard[0]] + letters[rearguard[1]]
    output = "Case #{}: {}".format(i+1, output)
    outputs.append(output)
    
for output in outputs:
    print(output)