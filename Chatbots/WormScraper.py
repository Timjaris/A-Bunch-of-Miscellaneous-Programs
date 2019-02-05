# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 18:19:29 2019

@author: Tim'
Okay, Nevermind, wildbow has built his website to make this as hard as possible
"""
from urllib.request import urlopen
import string
import sys
import math
import re
from bs4 import BeautifulSoup

chapter = "https://parahumans.wordpress.com/category/stories-arcs-1-10/arc-1-gestation/1-01/"
chapter = "https://parahumans.wordpress.com/2011/06/14/gestation-1-2/"

#AHAHAHA the entire point of this was to avoid the comments, but some TOC link
# include comments, it's just less often for some reason HAHAHA
toc = "https://parahumans.wordpress.com/table-of-contents/"
Toc = urlopen(toc)
toC = Toc.read()
TOC = BeautifulSoup(toC, 'html.parser')
tableOfContents = TOC.find_all("p")
ToC = []
useless = 0
for arc in tableOfContents:
    for chapter in arc.contents:
        try:
            link = chapter.contents[0].get('href')
            if link != None:
                print(link)
                ToC.append(link)
        except AttributeError:
            useless+=1
        except IndexError:
            useless+=10000
print(useless)


"""
f = open("Worm.txt", 'w')
for i in range(302):
    print("Progress:", i, " / ", 302)
    url = urlopen(chapter)
    page = url.read()
    soup = BeautifulSoup(page, 'html.parser')
    
    hope = soup.find_all("p")
    for line in hope:
        try:
            f.write(line.get_text())
            f.write('\n\n\n')
        except UnicodeEncodeError:
            print(repr(line))
            print("Stupid, stupid, dumb")
    chapter = hope[0].contents[0].get('href')
    
    
f.close()
print("Done!")
"""