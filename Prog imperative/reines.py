# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 09:14:09 2021

@author: notta
"""

R=[x for x in range(0,8)]
tab=[-1]*8
trouve=False

def acceptable(numReine,e):
    global R,tab
    res=True
    if e in tab:
        res=False
    for i in range(numReine):
        if abs(numReine-i)==abs(tab[i]-e):
            res=False
    return res
    

def placerReines(numReine):
    global R,tab,trouve
    if numReine==len(tab):
        trouve=True
        return
    for e in range(len(tab)):
        if acceptable(numReine,e):
            print(tab)
            tab[numReine]=e
            placerReines(numReine+1)
            if trouve:
                return tab
            tab[numReine]=-1

print(placerReines(0))