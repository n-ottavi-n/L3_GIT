# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 11:37:47 2021

@author: notta
"""
from Aterlier4_ex1 import full_name

def test_full_name():
    res=False
    nom="ottavi nicolas"
    attendu="OTTAVI Nicolas"
    resultat=full_name(nom)
    test=attendu==resultat
    print("attendu: {}, resultat: {}".format(attendu,resultat))
    if test:
        print("SUCCES")
        res=True
    else:
        print("ECHEC")
    return res