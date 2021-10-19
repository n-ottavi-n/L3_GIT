# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 08:59:29 2021

@author: notta
"""

import random as rd

def gen_list_random_int(int_nbr=10,int_binf=0,int_bsup=9)->list:
    """
    retourne une liste de 10 nombres aleatoires entre int_binf et int_bsup,
    entre 0 inclus et 10 exclus par defaut

    Parameters
    ----------
    int_binf : int, optional
        DESCRIPTION. The default is 0:int. valeur min
    int_bsup : int, optional
        DESCRIPTION. The default is 9:int. valeur max

    Returns
    -------
    list
        liste de 10 entiers entre int_binf et int_bsup

    """
    lst_res=[]
    for i in range(int_nbr):
        lst_res.append(rd.randint(int_binf,int_bsup))
    return lst_res

print(gen_list_random_int(1,5))