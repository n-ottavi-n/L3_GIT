# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 11:14:24 2021

@author: notta
"""

import random
import time

compt=0

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
    global compt
    lst=lst.copy()
    for i in range(0,len(lst)):
        ind_p=(i-1)//2 #indice du parent
        while(lst[i]<lst[ind_p] and ind_p>=0):#tant que l'element est inferieur a son parent et qu'on ne depasse pas le tableau par la gauche   
            lst[i], lst[ind_p]=lst[ind_p], lst[i]
            i=ind_p #maj de l'indice
            ind_p=(ind_p-1)//2 #on passe au parent du parent
            compt+=1
    return lst
            
    
    
    
def depiler(lst:list)->list: #FAUX
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
    lst=lst.copy()
    lst_res=[]
    for i in range(len(lst)):
        lst_res+=[lst[0]] #la liste triee/on met le meilleur element(le plus petit)
        lst[0]=lst[-1]#l'element le plus a droite vient au debut  
        lst=lst[:-1] #on enleve la derniere case
        lst=entasser(lst)#on ordonne le nouvel arbre
    return lst_res
    
def depilerCorrection(lst): #CORRECT
    for i in range(len(lst)-1,1):
        ind=0; f=i-1
        while(ind*2+1<=f):
            pp=ind*2+1
            if(ind+1)*2 <=f and lst[pp]>lst[(ind+1)*2]:
                pp=(ind+1)*2
            lst[ind],lst[pp]=lst[pp],lst[ind]
            ind=pp
    return lst
        
    
def triParTas(lst):
    lst_entassee=entasser(lst)
    return depilerCorrection(lst_entassee)

lst_test=random.sample(range(0,5000), 1000)

triParTas(lst_test)
print(compt)

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
'''
def perf_test(n):

    
    somme_classique=0
    somme_recur=0
    
    for i in range(n):        
        lst_test=random.sample(range(0,500), 100)    
    
        tick=time.perf_counter_ns()
        triParTas(lst_test)
        tock=time.perf_counter_ns()
        somme_classique+=(tock-tick)
        
        tick=time.perf_counter_ns()
        triParTasRec(lst_test)
        tock=time.perf_counter_ns()
        somme_recur+=(tock-tick)
        
    print("classique: {}\n recursif: {}".format(somme_classique/n,somme_recur/n))
    
perf_test(100)'''