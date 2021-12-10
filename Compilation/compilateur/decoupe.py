# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 11:19:16 2021

@author: notta
"""

import math

def decoupe(prix):
    bestPrix=[0]*len(prix)
    solution=[0]*len(prix)
    for i in range(1,len(prix)):
        maxPrix=-math.inf
        for j in range(1,i+1):
            if maxPrix<prix[j]+bestPrix[i-j]:
                maxPrix=prix[j]+bestPrix[i-j]
                solution[i]=j
            print(i)
            bestPrix[i]=maxPrix
    return bestPrix, solution
    
prix=[0,2,5,7,9,10,12,14,15]

print(decoupe(prix))