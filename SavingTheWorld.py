# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 13:41:59 2018

@author: Tim
"""
import sys

def getDamage(s):
    strenth = 1
    damage = 0
    for c in s:
        if c=='C':
            strenth*=2
        if c=='S':
            damage+=strenth
    return damage

def hack(s, pos):
    new = ''
    for i in range(len(s)):
        if i!=pos and i!=pos+1:
            new+=s[i]
        elif i==pos:
            new+=s[i+1]
        elif i==pos+1:
            new+=s[i-1]
    return new
            
    
#Okay, doing the rightmost one is better, but I already wrote this so...
def greedyBestHack(s):
    best = getDamage(s)
    result = s
    for i in range(len(s)-1):
        swapped = hack(s, i)
        d = getDamage(swapped)
        if d < best: 
            best=d
            result=swapped
    return result
        
        
        
T = sys.stdin.readline()
T = int(T)
for i in range(T):
    tmp = sys.stdin.readline()
    elms = tmp.split()
    D, P = (int(elms[0]), elms[1])
    D = int(D)
    
    hacks = 0
    improving = True
    damage = getDamage(P)
    while damage > D and improving:
        newDamage = getDamage(greedyBestHack(P))
        hacks+=1
        if newDamage == damage:
            improving = False
            print ("Case #"+str(i+1)+": "+"IMPOSSIBLE")
    if improving:
        print ("Case #"+str(i+1)+": "+str(hacks))
            