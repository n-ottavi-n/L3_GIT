# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 09:13:57 2021

@author: notta
"""
import random as rd

from Atelier5_ex1 import gen_list_random_int

def mix_list(list_to_mix:list)->list:
    """
    retourne une liste ou les element de la liste d'entree sont melanges, 
    n'affecte pas la liste d'entree

    Parameters
    ----------
    list_to_mix : list
        Liste d'entiers potentiellement triée'

    Returns
    -------
    list
        Liste melangée: lst_res

    """
    longueur=len(list_to_mix)
    lst_res=[0]*longueur    #initialisation de lst_res
    lst_new_indice=[] #liste des cases de lst_res qui ont deja ete remplies
    
    for indice in range(longueur):#parcours les indices de la liste d'entree
        new_indice=rd.randint(0, longueur-1)#recherche aleatoire d'un indice pour insertion dans la liste retournee
       
        while new_indice in lst_new_indice:#on verifie que new_indice n'a pas deja ete utilise
            new_indice=rd.randint(0, longueur-1)#sinon on en genere un autre
        
        lst_res[new_indice]=list_to_mix[indice]#l'element est place dans une case de lst_res choisie au hasard
        lst_new_indice.append(new_indice)#on ajoute new_indice a la liste pour ne pas le réutiliser
    
    return lst_res




lst_test=gen_list_random_int()
print(lst_test)
print(mix_list(lst_test))

