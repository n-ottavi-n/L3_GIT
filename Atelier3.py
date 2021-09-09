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

def somme_indices(L:list):
    somme=0
    for i in range(len(L)):
        somme+=L[i]
    return somme

def somme_elem(L:list):
    somme=0
    for l in L:
        somme+=l
    return somme

def somme_while(L:list):
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

def moyenne(L:list):
    """retourne la moyenne d'une liste
    input:
        L: [int]
    outputs:
        int: moyenne des valeurs de la liste/0 si liste vide"""
    somme=0
    if len(L)>0: #True si liste non vide
        for l in L:
            somme+=l
        somme=somme/len(L)
    return somme

ENTIERS=[]

#print(ENTIERS,"moyenne: ",moyenne(ENTIERS))

def nb_sup_elem(L:list,e:int):
    """retourne le nombres valeurs d'une liste strictement superieures a un entier
    --version elements--
    inputs:
        L: [int]
        e: int: entier dont on cherche le nombre de valeurs superieures dans la liste
    outputs:
        int: nombre de valeurs de L superieures a e"""
    somme=0
    if len(L)>0:#True si liste non vide
        for l in L:
            if l>e:
                somme+=1
    return somme

e=3
#print(ENTIERS,"nb d'entiers >{}:".format(e),nb_sup_elem(ENTIERS, e))

        
def nb_sup_ind(L:list,e:int):
    """retourne le nombres valeurs d'une liste strictement superieures à un entier
    --version indices--
    inputs:
        L: [int] liste
        e: int: entier dont on cherche le nombre de valeurs superieures dans la liste
    outputs:
        int: nombre de valeurs de L superieures a e"""
    somme=0
    longueur=len(L)
    if longueur>0:#True si liste non vide
        for i in range(longueur):
            if L[i]>e:
                somme+=1
    return somme

#print(ENTIERS,"nb d'entiers >{}:".format(e),nb_sup_ind(ENTIERS, e))

def moy_sup(L:list,e:int):
    """renvoie la moyenne des valeurs superieures a un entier dans une liste
    inputs:
        L: [int]
        e: int: entier dont on cherche la moyenne des valeurs superieures dans la liste
    outputs:
        int: moyenne des valeurs superieures a e"""
    moyenne=0
    if len(L)>0:#True si liste non vide
        diviseur=nb_sup_elem(L,e)
        for l in L:
            if l>e:
                moyenne+=l
        moyenne=moyenne/diviseur
    return moyenne

#print(ENTIERS,moy_sup(ENTIERS, e))
            
def val_max(L:list):
    """retourne la valeur max d'une liste d'entiers
    input:
        L: [int]
    output:
        int: valeur max de la liste"""
    res=0
    if len(L)>0:#True si liste non vide
        for l in L:
            if l>res:
                res=l
    return res

ENTIERS=[1,2,3,4,100,6]
#print(ENTIERS,"max: {}".format(val_max(ENTIERS)))      

def ind_max(L:list):
    """retourne l'indice de la valeur max d'une liste
    inputs: 
        L: [int]
    outputs:
        int: valeur max de L"""
    maxi=val_max(L)
    res=0
    for i in range(len(L)):
        if L[i]==maxi:
            res=i
    return res

ENTIERS=[]

print(ENTIERS,"indice du max: ", ind_max(ENTIERS))

        
