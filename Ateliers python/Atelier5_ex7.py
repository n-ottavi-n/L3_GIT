# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 20:19:02 2021

@author: notta
"""

#Tri stupide

def est_triee(lst_quelconque:list)->bool:
    """
    Renvoie True si la liste est triee

    Parameters
    ----------
    lst_quelconque : list
        DESCRIPTION.

    Returns
    -------
    bool
        DESCRIPTION.

    """
    res=True
    i=0
    while res and i<len(lst_quelconque)-1:
        if lst_quelconque[i+1]<lst_quelconque[i]:
            res=False
        i+=1
    return res

from Atelier5_ex2 import mix_list
from Atelier5_ex1 import gen_list_random_int

def tri_stupide(lst_a_trier:list)->list:
    """
    randomise une liste jusqu'a ce qu'elle sout triée

    Parameters
    ----------
    lst_a_trier : list
        liste a trier

    Returns
    -------
    list
        liste triee

    """
    lst_rand=lst_a_trier.copy()
    succes=est_triee(lst_rand)
    while not succes:
        lst_rand=mix_list(lst_rand)
        print(lst_rand)
        succes=est_triee(lst_rand)
    return lst_rand

len_lst=10
lst_test=gen_list_random_int(0,len_lst)

#print(tri_stupide(lst_test))

#Tri par insertion

def insertion_sort(lst_a_trier:list)->list:
    """
    tri par insertion

    Parameters
    ----------
    lst_a_trier : list
        DESCRIPTION.

    Returns
    -------
    list
        liste triée

    """
    lst_triee=lst_a_trier.copy()
    n=len(lst_a_trier)
    for indice in range(1,n):
        valeur=lst_triee[indice]
        j=indice
        while j>0 and lst_triee[j-1]>valeur:
            lst_triee[j]=lst_triee[j-1]
            j-=1
        lst_triee[j]=valeur
        print(lst_triee)
    return lst_triee

#print(lst_test,"->",insertion_sort(lst_test))
    
def selection_sort(lst_a_trier:list)->list:
    """
    tri par selection

    Parameters
    ----------
    lst_a_trier : list
        DESCRIPTION.

    Returns
    -------
    list
        liste triée

    """    
    lst_triee=lst_a_trier.copy()
    n=len(lst_a_trier)
    for i in range(n):#boucle sur toute la liste
        mini=i #indice du plus petit element de la partie non triee
        for j in range(i+1, n):#boucle sur la partie non triee
            if lst_triee[j]<lst_triee[mini]:
                mini=j#nouvelle valeur mini
        if mini!=i:
            lst_triee[i], lst_triee[mini]=lst_triee[mini], lst_triee[i]#on interverti
    return lst_triee

#print(lst_test,"->",selection_sort(lst_test))

#Tri a bulle

def bubble_sort(lst_a_trier:list)->list:
    """
    tri a bulle

    Parameters
    ----------
    lst_a_trier : list
        DESCRIPTION.

    Returns
    -------
    list
        liste triee

    """
    lst_triee=lst_a_trier.copy()
    n=len(lst_a_trier)
    for i in range(n,1,-1):#boucle sur la liste
        triee=True
        for j in range(i-1):#boucle sur la partie non triee
            if lst_triee[j+1]<lst_triee[j]:
                lst_triee[j], lst_triee[j+1]=lst_triee[j+1], lst_triee[j]
                triee=False
        if triee:
            return lst_triee
"""
print('Avant tri :',lst_test)
print('Resultat du tri :', bubble_sort(lst_test))
print('Après le tri la liste d\'origine n\'a pas été modifiée:',lst_test)
"""

def merge(lst_a:list,lst_b:list)->list:
    """
    retourne une liste triee des elements de a et b

    Parameters
    ----------
    lst_a : list
        liste triee
    lst_b : list
        liste triee

    Returns
    -------
    list
        liste triee des elements de list_a et de list_b

    """
    if not lst_a:
        return lst_b
    elif not lst_b:
        return lst_a
    elif lst_a[0]<lst_b[0]:
        return [lst_a[0]]+merge(lst_a[1:],lst_b)
    else:
        return [lst_b[0]]+merge(lst_a, lst_b[1:])
    
    

def merge_sort(lst_a_trier:list)->list:
    """
    tri fusion

    Parameters
    ----------
    lst_a_trier : list
        DESCRIPTION.

    Returns
    -------
    list
        liste triee

    """
    lst_triee=lst_a_trier.copy()
    n=len(lst_a_trier)
    if n<=1:
        return lst_triee
    else:
        return merge(merge_sort(lst_triee[:n//2]),merge_sort(lst_triee[(n//2):]))
"""
print('Avant tri :',lst_test)
print('Resultat du tri :', merge_sort(lst_test))
print('Après le tri la liste d\'origine n\'a pas été modifiée:',lst_test)
"""

def radix_order_sort(lst_a_trier:list,order:int)->list:
    """
    tri une liste d'entier a un certain order (par unite, dizaine, centaine,...)

    Parameters
    ----------
    lst_a_trier : list
        DESCRIPTION.
    order : int
        ordre du tri

    Returns
    -------
    list
        liste triee

    """
    for i in range(len(lst_a_trier)):
        

def radix_sort(lst_a_trier:list)->list:
    """
    tri par base

    Parameters
    ----------
    lst_a_trier : list
        DESCRIPTION.

    Returns
    -------
    list
        liste triée

    """
    lst_triee=lst_a_trier.copy()
    for order in range(3):
        lst_triee=radix_order_sort(lst_triee,order)
    return lst_triee
        