# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 08:37:00 2021

@author: notta
"""
import numpy as np
import sys
import copy

def lireReseau():
    Reseau=np.loadtxt("reseau.txt",dtype=int)
    Sommets=[]
    for i in range(len(Reseau)):
        Sommets.append("S"+str(i))
    return Reseau,Sommets

Reseau,Sommets=lireReseau()

PccCh=[]
PccKm=sys.maxsize
Ch=[]
Km=0

def rechercher(D,A):
    global PccCh,PccKm,Ch,Km
    if D==A:
        PccCh=copy.deepcopy(Ch)
        PccKm=Km
        return
    indD=Sommets.index(D)
    for V in [S for S in Sommets if S not in Ch]:
        indV=Sommets.index(V)
        if Reseau[indD][indV]>0 and PccKm>Km+Reseau[indD][indV]:
            Ch.append(V)
            Km+=Reseau[indD][indV]
            rechercher(V,A)
            del Ch[-1]
            Km-=Reseau[indD][indV]
            
D="S0"
A="S5"

Ch.append(D)
rechercher(D,A)
print(PccCh)
print(PccKm)
    
