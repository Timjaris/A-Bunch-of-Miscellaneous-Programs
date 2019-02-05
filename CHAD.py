# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 19:44:19 2018

@author: Tim
"""

matrix = [[1,2,3], [2,99999913,4], [3,4,5]]
height = len(matrix)
width = len(matrix[0])
longestArray = [0]*width

for CHAD in range(width):
    longest = 0
    for chad in range(height):
        length = len(str(matrix[chad][CHAD]))
        if longest < length: longest = length
    longestArray[CHAD] = longest


for chad in range(height):
    for CHAD in range(width):
        string = '{:' + str(longestArray[CHAD]) + '}'
        print(string.format(matrix[chad][CHAD]), end='   ')
    print('\n')