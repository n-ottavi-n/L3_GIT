# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 10:31:26 2021

@author: notta
"""
import numpy as np

Mat=np.loadtxt("sudoku.txt",dtype=int)



trouve=False
cases=np.where(Mat==0) #cases vides

def chiffres_ligne(Mat,i):
    return [x for x in Mat[i] if x>0]

def chiffres_colonne(Mat,i):
    return[x for x in Mat[0:,i] if x>0]

def chiffres_bloc(Mat,i,j):
    L=[]
    for x in range(3*(i//3),3*(i//3)+3):
        for y in range(3*(j//3),3*(j//3)+3):
            L=L+[Mat[x,y] if Mat[x,y]>0]
    

def chiffres_conflit(Mat,i,j):


#def sudoku(grille,casesVides,)