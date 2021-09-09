# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 10:49:11 2021

@author: notta
"""
import random

def plusoumoins(min:int,max:int):
    randomNumber=random.randint(min,max)
    finDuJeu=False
    coup=1
    while not(finDuJeu) and (coup<11):
        monNbr=int(input("Entrez un nombre: "))
        if(monNbr>randomNumber):
            print("trop grand")
        elif(monNbr<randomNumber):
            print("trop petit")
        else:
            print("Tu gagnes en ",coup," coup(s)")
            finDuJeu=True
        coup+=1
    if(coup>10):
        print("perdu")
        
#plusoumoins(0, 10)

#test modif github

#EXERCICE 1

ENTIERS=[1,2,3,4,5]

def somme_indices(L):
    somme=0
    for i in range(len(L)):
        somme+=L[i]
    return somme

def somme_elem(L):
    somme=0
    for l in L:
        somme+=l
    return somme

def somme_while(L):
    somme=0
    ind=len(L)-1
    while ind>=0:
        somme+=L[ind]
        ind-=1
    return somme

#print(somme_indices(ENTIERS))
#print(somme_elem(ENTIERS)) 
#print(somme_while(ENTIERS))       

def test_exercice1 ():
    print("TEST SOMME")
    #test liste vide
    print("Test liste vide : ", somme_while([]))
    #test somme 11111
    S=[1,10,100, 1000,10000]
    print("Test somme 1111 : ", somme_while(S))
    
#test_exercice1()

def moyenne(L):
    somme=0
    if len(L)>0:
        for l in L:
            somme+=l
        somme=somme/len(L)
    return somme

ENTIERS=[]

print(ENTIERS,"moyenne: ",moyenne(ENTIERS))


