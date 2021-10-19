# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 14:36:40 2021

@author: notta
"""

def hanoi(n,ta,tb,tc,nomA,nomB,nomC):
    if n==1:
        print(ta[-1],nomA," =>",nomB)
        tb.append(ta[-1])
        del ta[-1]
    else:
        hanoi(n-1,ta,tc,tb,nomA,nomC,nomB)
        hanoi(1,ta,tb,tc,nomA,nomB,nomC)
        hanoi(n-1,tc,tb,ta,nomC,nomB,nomA)
        
n=5
ta=[x for x in range(n,0,-1)]
tb=[]
tc=[]

print("A: {}, B: {}, C: {}".format(ta,tb,tc))

hanoi(ta[0],ta,tb,tc,"A","B","C")

print("A: {}, B: {}, C: {}".format(ta,tb,tc))