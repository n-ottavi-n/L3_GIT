# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 09:14:17 2021

@author: notta
"""
from Atelier5_ex2 import mix_list

def test_mix_list():
    lst_sorted=[i for i in range(10)]
    sauvegarde_ls=lst_sorted
    print(lst_sorted)
    print('Liste triée de départ',lst_sorted)
    mixed_list=mix_list(lst_sorted)
    print('Liste mélangée obtenue',mixed_list)
    print('Liste triée de départ après appel à mixList, elle doit êtreinchangée',lst_sorted)
    #assert (cf. doc en ligne) permet de vérifier qu’une condition
    #est vérifiée en mode debug (désactivable)
    assert lst_sorted != mixed_list,"Les deux listes doivent être différenteaprès l'appel à mixList..."
    return lst_sorted!=mixed_list and lst_sorted==sauvegarde_ls
    
print(test_mix_list())