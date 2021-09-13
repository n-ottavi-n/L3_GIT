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
    moyenne=0
    if len(L)>0:
        moyenne=somme_elem(L)/len(L)
    return moyenne

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



        
#EXERCICE2

def position_for(lst:list,elem:int):
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

def position_while(lst:list, elem:int):
    """retourne l'indice de l'element elem dans la liste lst
    --version while--
    inputs:
        lst: [int] la liste
        elem: int element dont on cherche la position
    outputs:
        int: l'indice de l'element, -1 si element absent"""
    i=0 #on commence a l'indice 0
    if len(lst)==0: #cas liste vide
        return -1
    else: #cas liste non vide
        val=lst[0]
        while val!=elem:
            if i<len(lst)-1:
                    i+=1
                    val=lst[i]
                    print(i)
            else: #elem non present dans la liste
                return -1
    return i

e=10

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
        while lst[i]>lst[i-1]:#test element par element
            if i<len(lst)-1:
                i+=1
            else:#on est arrives au bout de la liste
                return True
        else: #un element est superieur au suivant
            res=False
    return res

ENTIERS=[1,2,3,6]

#print(ENTIERS, est_trie_while(ENTIERS))
    
def position_tri(lst:list,elem:int)->int:
    """retourne la position de l'entier elem dans une liste triee, utilise une recherche dichotomique    

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
    pos=fin//2#initialise pos
    while lst[pos]!=elem:
        #print(lst[pos])
        if lst[pos]<elem:
            debut=pos
        else:
            fin=pos
        pos=(fin-debut)//2
        #print("pos: ",pos)
    return pos
    
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
        else: #repetition
            res=True
        i+=1
    return res

ENTIERS=[1,2,6,3,4]

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

print(separer(LST))

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
    
    
    

  
