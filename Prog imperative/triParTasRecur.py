# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 14:16:54 2021

@author: notta
"""
import random

def entasser(lst:list)->list:
    """
    retourne une liste sous forme d'un arbre ordonné'
    Parameters
    ----------
    lst : list
        liste d'entrée desordonnée

    Returns
    -------
    list
        arbre ordonné

    """
    lst=lst.copy()
    for i in range(0,len(lst)):
        ind_p=(i-1)//2 #indice du parent
        while(lst[i]<lst[ind_p] and ind_p>=0):#tant que l'element est inferieur a son parent et qu'on ne depasse pas le tableau par la gauche   
            lst[i], lst[ind_p]=lst[ind_p], lst[i]
            i=ind_p #maj de l'indice
            ind_p=(ind_p-1)//2 #on passe au parent du parent
    return lst
            
    
    
    
def depilerRec(lst:list)->list:
    """
    retourne une liste triée a partir d'un arbre ordonné'

    Parameters
    ----------
    lst : list
        arbre ordonné

    Returns
    -------
    list
        liste triée croissante

    """
    if len(lst)==0:
        return []
    else:
        lst_res=[lst[0]]
        lst[0]=lst[-1]#l'element le plus a droite vient au debut  
        lst=lst[:-1] #on enleve la derniere case
        lst=entasser(lst)#on ordonne le nouvel arbre
        return lst_res+depilerRec(lst)    
        
    
def triParTasRec(lst):
    lst_entassee=entasser(lst)
    return depilerRec(lst_entassee)


#lst_test=[9,6,21,3,4,12,11,8]
lst_test=random.sample(range(0,50), 10)

print(lst_test)

print(triParTasRec(lst_test))