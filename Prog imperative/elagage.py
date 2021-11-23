# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 09:31:58 2021

@author: notta
"""

import math
import copy
        

class Noeud():
    def __init__(self,G, D, val=math.inf):
        self.D=D
        self.G=G
        self.val=val
        
    def isFeuille(self):
        if self.D==None and self.G==None:
            return True
        return False
    
V=[7,9,5,4,11,13,4,17,5,9,4,2,11,1,13,6]

def createTree(V):
    Nd=[]
    for i in range(len(V)):
        Nd.append(Noeud(None,None,V[i]))
    continu=True
    while(continu):
        Parents=[]
        for i in range(0,len(Nd),2):
            Parents.append(Noeud(Nd[i],Nd[i+1]))
        if len(Parents)==1:
            continu=False
        else:
            Nd=copy.deepcopy(Parents)
            Parents.clear()
    return Parents[0]
        
A=createTree(V)
    

def elagage(N, depth=0, alpha=-math.inf, beta=math.inf):
    if N.isFeuille():
        return N.val
    successeurs=[N.G,N.D]
    if (depth%2==0):
        maxValue=-math.inf
        for s in successeurs:
            value=elagage(s,depth+1,alpha,beta)
            maxValue=max(maxValue,value)
            alpha=max(alpha,value)
            if beta<=alpha:
                break
        return maxValue
    else:
        minValue=math.inf
        for s in successeurs:
            value=elagage(s,depth+1,alpha,beta)
            minValue=min(minValue,value)
            beta=min(beta,value)
            if beta<=alpha:
                break
        return minValue
 
elagage(A)
    