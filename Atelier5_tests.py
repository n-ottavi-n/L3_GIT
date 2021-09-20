# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 09:14:17 2021

@author: notta
"""
from Atelier5_ex2 import mix_list
"""
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
"""
from Atelier5_ex3 import choose_element_list

lst_sorted=[0,1,2,3,4,5,6,7,8,9]
"""
print('Liste triée de départ',lst_sorted)
e1 = choose_element_list(lst_sorted)
print('A la première exécution',e1,'a été sélectionné')
e2 = choose_element_list(lst_sorted)
print('A la deuxième exécution',e2,'a été sélectionné')
assert e1 != e2#"Attention vérifiez votre code, pour deux sélections de
#suite l'élément sélectionné est le même !"

print('Liste de départ',lst_sorted)
sublist = extract_elements_list(lst_sorted,5)
print('La sous liste extraite est',sublist)
print('Liste de départ après appel de la fonction est',lst_sorted)
"""

from Atelier5_ex4 import extract_element_list

print('Liste de départ',lst_sorted)
sublist = extract_element_list(lst_sorted,5)
print('La sous liste extraite est',sublist)
print('Liste de départ après appel de la fonction est',lst_sorted)