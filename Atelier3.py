# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 10:49:11 2021

@author: notta
"""
import random

def plusoumoins(mini:int,maxi:int):
    randomNumber=random.randint(mini,maxi)
    finDuJeu=False
    coup=1
    while not(finDuJeu) and (coup<11):
        monNbr=int(input("Entrez un nombre: "))
        if monNbr>randomNumber:
            print("trop grand")
        elif monNbr<randomNumber:
            print("trop petit")
        else:
            print("Tu gagnes en ",coup," coup(s)")
            finDuJeu=True
        coup+=1
    if coup>10:
        print("perdu")

#plusoumoins(0, 10)

#test modif github

#EXERCICE 1

ENTIERS=[1,2,3,4,5]

def somme_indices(L:list)->int:
    """
    retourne la somme des elements d'une liste
    --version indices--

    Parameters
    ----------
    L : list
        liste d'entiers

    Returns
    -------
    int
        somme des elements

    """
    somme=0
    for i in range(len(L)):
        somme+=L[i]
    return somme

def somme_elem(L:list)->int:
    """
    retourne la somme des elements d'une liste
    --version elements--

    Parameters
    ----------
    L : list
        liste d'entiers

    Returns
    -------
    int
        somme des elements

    """
    somme=0
    for l in L:
        somme+=l
    return somme

def somme_while(L:list)->int:
    """
    retourne la somme des elements d'une liste
    --version while--

    Parameters
    ----------
    L : list
        liste d'entiers

    Returns
    -------
    int
        somme des elements

    """
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
    print("Test somme 11111 : ", somme_while(S))

#test_exercice1()

def moyenne(L:list)->int:
    """retourne la moyenne d'une liste
    input:
        L: [int]
    outputs:
        int: moyenne des valeurs de la liste/0 si liste vide"""
    moy=0
    if L !=[]:
        moy=somme_elem(L)/len(L)
    return moy

ENTIERS=[]

#print(ENTIERS,"moyenne: ",moyenne(ENTIERS))

def nb_sup_elem(L:list,e:int)->int:
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


def nb_sup_ind(L:list,e:int)->int:
    """retourne le nombres de valeurs d'une liste strictement superieures à un entier
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

def moy_sup(L:list,e:int)->float:
    """renvoie la moyenne des valeurs superieures a un entier dans une liste
    inputs:
        L: [int]
        e: int: entier dont on cherche la moyenne des valeurs superieures dans la liste
    outputs:
        float: moyenne des valeurs superieures a e"""
    moyenne=0
    if len(L)>0:#True si liste non vide
        diviseur=nb_sup_elem(L,e)
        for l in L:
            if l>e:
                moyenne+=l
        moyenne=moyenne/diviseur
    return moyenne

#print(ENTIERS,moy_sup(ENTIERS, e))

def val_max(L:list)->int:
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

def ind_max(L:list)->int:
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




#EXERCICE2

def position_for(lst:list,elem:int)->int:
    """retourne l'indice de l'element elem dans la liste lst
    --version for--
    inputs:
        lst: [int] la liste
        elem: int element dont on cherche la position
    outputs:
        int: l'indice de l'element/-1 si element absent"""
    res=-1
    for i in range(len(lst)):
        if lst[i]==elem:
            res=i
    return res

def position_while(lst:list, elem:int)->int: ####A CORRIGER#####
    """retourne l'indice de l'element elem dans la liste lst
    --version while--
    inputs:
        lst: [int] la liste
        elem: int element dont on cherche la position
    outputs:
        int: l'indice de l'element, -1 si element absent"""
    res=-1
    i=0 #on commence a l'indice 0
    if len(lst)!=0: #cas liste non vide
        val=lst[0]
        while val!=elem and i<len(lst)-1:
            res=i
            i+=1
            val=lst[i]
        else:
            res=i
    return res

e=11
ENTIERS=[1,2,3,10,5,6,4]
#print(ENTIERS,"position: ", position_while(ENTIERS,e))

def nb_occurrences(lst:list,elem:int)->int:
    """renvoie le nombre d'occurrences d'un entier dans une liste

    Parameters
    ----------
    lst : [int]
        la liste
    elem : int
        entier dont on cherche le nombre d'occurences

    Returns
    -------
    int
        nb d'occurrences de elem

    """
    somme=0
    if len(lst)>0:
        for e in lst:
            if e==elem:
                somme+=1
    return somme

e=0
ENTIERS=[10,0,10,2,10,1]
#print(ENTIERS,"nb_occ de {}: ".format(e), nb_occurrences(ENTIERS,e))

def est_trie_for(lst:list)->bool:
    """retourne vrai si la liste passee en parametre est triee
    --version for--

    Parameters
    ----------
    lst : [int]
        liste d'entiers'

    Returns
    -------
    bool
        True si la lsite est triee

    """
    res=True
    for i in range(1,len(lst)):
        if lst[i]<lst[i-1]:
            res=False
    return res

def est_trie_while(lst:list)->bool:
    """retourne vrai si la liste passee en parametre est triee
    --version while--

    Parameters
    ----------
    lst : [int]
        liste d'entiers'

    Returns
    -------
    bool
        True si la lsite est triee ou vide

    """
    res=True
    i=1
    if len(lst)>0:
        while lst[i]>=lst[i-1] and i<len(lst)-1:#test element par element
            i+=1
        else: #un element est superieur au suivant ou on est arrive en fin de liste
            if i<len(lst)-1: #True si on est pas arrivé jusqu'a la fin
                res=False
    return res

ENTIERS=[1,2,3]

#print(ENTIERS, est_trie_while(ENTIERS))

def position_tri(lst:list,elem:int)->int: ####PROBLEME DE DICHOTOMIE####
    """retourne la position de l'entier elem dans une liste triee,
    utilise une recherche dichotomique

    Parameters
    ----------
    lst : [int]
        liste d'entier a explorer
    elem : int
        element dont on cherche la position

    Returns
    -------
    int
        indice de elem dans la liste

    """
    debut=0 #debut de l'intervalle de recherche
    fin=len(lst)#fin de l'intervalle de recherche
    pos=-1#initialise pos
    if lst:
        pos=fin//2
        while lst[pos]!=elem:
            #print(lst[pos])
            if lst[pos]<elem:
                debut=pos
            else:
                fin=pos
            pos=(fin-debut)//2
            #print("pos: ",pos)
    return pos

ENTIERS=[]
#print(position_tri(ENTIERS, 1))

def a_repetition(lst:list)->bool:
    """retourne True si la liste passee en parametre comporte une ou plusieurs repetitions


    Parameters
    ----------
    lst : list
        liste d'entiers a evaluer

    Returns
    -------
    bool
        true si il y a une repetition

    """
    res=False
    lst_t=[]
    i=0
    while i<len(lst) and not res:
        if lst[i] not in lst_t: #pas de repetition
            lst_t.append(lst[i])
            i+=1
        else: #repetition
            res=True
    return res

ENTIERS=[1,2,6,3]

#print(a_repetition(ENTIERS))

#EXERCICE 3

def separer(lst:list)->list:
    """
    renvoie une liste ou les nombres sont regroupes selon qu'ils sont negatifs, nuls ou positifs

    Parameters
    ----------
    lst : list
        liste d'entiers

    Returns
    -------
    list
        liste d'entiers regroupes

    """
    lst_sep=[]
    #generation de lst_sep
    for l in lst:
        lst_sep.append(0)
        #lst_sep=[0,0,0,..,0] len= len(lst)
    ind_n=0 #indice des nb negatifs (commence au debut)
    ind_p=len(lst)-1 #indice des nb positifs (commence a la fin)
    for i in range(len(lst)):
        if lst[i]<0:
            lst_sep[ind_n]=lst[i]
            ind_n+=1
        elif lst[i]>0:
            lst_sep[ind_p]=lst[i]
            ind_p-=1
    return lst_sep


LST=[-1,2,-12,0,4,0,5,-6]

def test_separer():
    """teste la fonction separer()"""
    #test liste vide, res attendu: []
    LST=[]
    print("liste vide: ",separer(LST))
    #test liste normal, res attendu: [-1,-12,-6,0,0,5,4,2]
    LST=[-1,2,-12,0,4,0,5,-6]
    print("[-1,2,-12,0,4,0,5,-6]: ",)
    #test liste entiers positifs, res attendu: [1,2,3]
    LST=[1,2,3]
    print("[1,2,3]", separer(LST))

#print(separer(LST))

#EXERCICE 4

def histo(lst_f:list)->list:
    """renvoie une liste d'entiers representant l'histogramme d'une fonction


    Parameters
    ----------
    lst_f : list
        liste d'entiers definissant une fonction

    Returns
    -------
    list
        liste d'entiers representant l'histogramme de lst_f

    """
    #initialisation de list_h
    lst_h=[]
    MAXVALEUR=val_max(lst_f)
    for i in range(MAXVALEUR+1):
        lst_h.append(0)
    #creation de l'histogramme
    for j in range(len(lst_f)): #parcours de lst_f
        valeur=lst_f[j] #recuperation de la valeur
        lst_h[valeur]+=1 #on increment l'entier d'indice correspondant la valeur
    return lst_h
    
LST=[6,5,6,8,4,2,1,5]
    
def est_injective(lst_f:list)->bool:
    """
    renvoie True si la fonction lst_f est injective, False sinon

    Parameters
    ----------
    lst_f : list
        liste d'entiers decrivant la fonction

    Returns
    -------
    bool
        True si injective, False sinon

    """
    res=True
    lst_h=histo(lst_f)
    termine=False
    i=0
    while not termine and lst_h[i]<2:
        i+=1
        if i==len(lst_h):
            termine=True
    else:
        if not termine:
            res=False
    return res

lst_f1=[6,5,6,7,4,2,1,5]
lst_h1=[0,1,1,0,1,2,2,1]

lst_f2=[3,0,6,7,4,2,1,5]
lst_h2=[1,1,1,1,1,1,1,1]

lst_fnull=[]
#print(est_injective(lst_fnull))

    
def est_surjective(lst_f:list)->bool:
    """
    renvoie True si la fonction lst_f est injective, False sinon

    Parameters
    ----------
    lst_f : list
        liste d'entiers decrivant la fonction

    Returns
    -------
    bool
        True si injective, False sinon

    """
    res=True
    lst_h=histo(lst_f)
    termine=False
    i=0
    while not termine and lst_h[i]>0:
        i+=1
        if i==len(lst_h):
            termine=True
    else:
        if not termine:
            res=False
    return res   

#print(est_surjective(lst_fnull))  

def est_bijective(lst_f:list)->bool:
    return est_injective(lst_f) and est_surjective(lst_f)

def affiche_histo(lst_f:list):
    lst_h=histo(lst_f)
    MAXOCC=val_max(lst_h) #nb de lignes
    MAXVALEUR=val_max(lst_f) #nb de colonnes
    print("HISTOGRAMME")
    print(lst_f)
    for ligne in range(MAXOCC):
        print("\n")
        for colonne in range(MAXVALEUR+1):
            if lst_h[colonne]>=MAXOCC-ligne: #premiere ligne: MAXOCC-0, deuxieme ligne: MAXOCC-1, ...
                print("  # ",end='')
            else:
                print('    ',end='')
    for i in range(MAXVALEUR+1):
            print('|--|',end='')
    print("\n")
    for j in range(MAXVALEUR+1):
            print("  {} ".format(j),end='')
            
    
                
    
F=[1,5,5,5,9,11,11,15,15,15]
#affiche_histo(F)

import matplotlib.pyplot as plt
    
def affiche_histo_plt(lst_f:list):
    print("HISTOGRAMME")
    print(lst_f)
    print(plt.hist(lst_f))

affiche_histo_plt(F)
