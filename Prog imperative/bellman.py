# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 09:35:38 2021

@author: notta
"""
import numpy as np
gamma=0.95
iterations=100

P=[[["sud", 3, 0.5, 4, 0.5],["est", 1, 0.7, 4, 0.3]],
   [["ouest", 0, 0.7, 3, 0.3],["sud", 3, 0.25, 4, 0.5, 5, 0.25],["est", 2, 0.7, 5, 0.3]],
   [["ouest", 1, 0.7, 4, 0.3],["sud", 4, 0.5, 5, 0.5]],
   [["nord", 0, 0.5, 1, 0.5],["sud", 6, 0.5, 7, 0.5],["est", 1, 0.25, 4, 0.5, 7, 0.25]],
   [["nord", 0, 0.25, 1, 0.5, 2, 0.25],["sud", 6, 0.25, 7, 0.5, 8, 0.25],["ouest", 0, 0.25, 3, 0.5, 6, 0.25],["est", 2, 0.25, 5, 0.5, 8, 0.25]],
   [["ouest", 1, 0.25, 4, 0.5, 7, 0.25],["nord", 1, 0.3, 2, 0.7],["sud", 7, 0.7, 8, 0.3]],
   [["nord", 3, 0.5, 4, 0.5],["est", 4, 0.3, 7, 0.7]],
   [["ouest", 3, 0.3, 6, 0.7],["nord", 3, 0.25, 4, 0.5, 5, 0.25],["est", 5, 0.3, 8, 0.7]],
   [["nord", 4, 0.5, 5, 0.5],["ouest", 4, 0.3, 7, 0.7]]
   ]

R=[[["sud", 3, 0, 4, 0],["est", 1, 0, 4, 0]],
   [["ouest", 0, 0, 3, 0],["sud", 3, 0, 4, 0, 5, 0],["est", 2, 0, 5, 0]],
   [["ouest", 1, 0, 4, 0],["sud", 4, 0, 5, 0]],
   [["nord", 0, 0, 1, 0.5],["sud", 6, 0, 7, 0],["est", 1, 0, 4, 0, 7, 0]],
   [["nord", 0, 0, 1, 0, 2, 0],["sud", 6, 0, 7, 0, 8, 0],["ouest", 0, 0, 3, 0, 6, 0],["est", 2, 0, 5, 0, 8, 0]],
   [["ouest", 1, 0, 4, 0, 7, 0],["nord", 1, 0, 2, 0],["sud", 7, 0, 8, 0]],
   [["nord", 3, 0, 4, 0],["est", 4, 0, 7, 0]],
   [["ouest", 3, 0, 6, 0],["nord", 3, 0, 4, 0, 5, 0],["est", 5, 0, 8, 0]],
   [["nord", 4, 0, 5, 0],["ouest", 4, 1, 7, 0]]
   ]

Q=[]

for s in range(len(P)):
    Q.append([0]*len(P[s]))
    
for i in range(iterations):
    for s in range(len(P)): #boucle sur les sommets
        for a in range(len(P[s])): #boucle sur les actions
            somme=0
            for ind in range(1,len(P[s][a]),2):
                s_next=P[s][a][ind]
                somme+=P[s][a][ind+1]*(R[s][a][ind+1]+gamma*np.max(Q[s_next]))
            Q[s][a]=somme

for s in range(len(P)):
    for a in range(len(P[s])):
        txt= f"Q[etat={s}, action={P[s][a][0]} = {Q[s][a]:.2f}"
        if a == np.argmax(Q[s]):
            txt=txt+"<="
        print(txt)
            