# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 09:36:29 2021

@author: notta
"""

import random 

def choose_element_list(list_in_which_to_choose:list)->any:
    """
    retourne un element pris au hasard de la liste passée en parametre

    Parameters
    ----------
    list_in_which_to_choose : list
        liste de n'importe quoi

    Returns
    -------
    any
        un element de la liste pris au hasard

    """
    return list_in_which_to_choose[random.randint(0,len(list_in_which_to_choose)-1)]

