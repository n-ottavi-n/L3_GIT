# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 20:19:02 2021

@author: notta
"""

import random

def extract_element_list(list_in_which_to_choose:list,int_nbr_of_element_to_extract:int)->list:
    """
    Retourne une liste de taille int_nbr_of_elements_to_extract d'elements de list_in_which_to_choose

    Parameters
    ----------
    list_in_which_to_choose : list
        liste d'elements
    int_nbr_of_element_to_extract : int
        nombres d'elements a extraire

    Returns
    -------
    list
        liste d'elements de la liste en parametre

    """
    lst_res=[]
    for i in range(int_nbr_of_element_to_extract):
        lst_res.append(list_in_which_to_choose[random.randint(0,len(list_in_which_to_choose)-1)])
    return lst_res