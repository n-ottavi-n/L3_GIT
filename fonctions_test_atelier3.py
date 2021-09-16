# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 13:46:46 2021

@author: notta
"""
from Atelier3 import separer

def test_separer():
    """teste la fonction separer()"""
    
    res="#####ECHEC#####"
    
    #test liste vide
    LST=[]
    test=separer(LST)
    attendu=[]
    test1=(attendu==test)#True si test reussi
    
    print("attendu: {}\nresultat: {}".format(attendu,test))  
    print(test1,"\n-------")
    
    #test liste normal, 
    LST=[-1,2,-12,0,4,0,5,-6]
    test=separer(LST)
    attendu=[-1, -12, -6, 0, 0, 5, 4, 2]
    test2=(attendu==test)#True si test reussi
    
    print("attendu: {} \nresultat: {}".format(attendu,test))    
    print(test2,"\n-------")
    
    #test liste entiers positifs, 
    LST=[1,2,3]
    test=separer(LST)
    attendu=[3,2,1]
    test3=(attendu==test)#True si test reussi
    
    print("attendu: {}\nresultat: {}".format(attendu,test))
    print(test3,"\n-------")
    
    #test lsite de 0
    LST=[0,0,0,0]
    test=separer(LST)
    attendu=[0,0,0,0]
    test4=(attendu==test)#True si test reussi
    
    print("attendu: {}\nresultat: {}".format(attendu,test))
    print(test4,"\n-------")
    
    if test1 and test2 and test3 and test4:
        res="#####SUCCES#####"
    print(res)
    
    
#print(test_separer())

#def test_separer2():
    

    
'''
from Atelier3 import est_trie_while as est_triee

def test_est_triee() -> bool:
    """
    Fonction de test si une liste est triée
    Returns:
        bool: True si tous les tests sont validés. False sinon
    """
    LISTE_VIDE = []

    LISTE_PAS_TRIEE1 = [5,3,1,2,9,8]
    LISTE_PAS_TRIEE2 = [1,2,-15,-2,9,-8]
    LISTE_PAS_TRIEE3 = [-1,-2,19,-19,-9,8]

    LISTE_TRIEE1 = [1,2,3,4,5]
    LISTE_TRIEE2 = [10,200,3565,42535,598387]
    LISTE_TRIEE3 = [-19,-6,77,77,77,77,88]

    fonction_valide = True

    # Triée #
    print("Resultat attendu : True")
    print("Test 1 : {}, obtenu : {}".format(LISTE_TRIEE1,est_triee(LISTE_TRIEE1)))
    print("Test 2 : {}, obtenu : {}".format(LISTE_TRIEE2,est_triee(LISTE_TRIEE2)))
    print("Test 3 : {}, obtenu : {}".format(LISTE_TRIEE3,est_triee(LISTE_TRIEE3)))

    if not est_triee(LISTE_TRIEE1) or not est_triee(LISTE_TRIEE2) or not est_triee(LISTE_TRIEE3):
        fonction_valide = False

    # Non Triée#
    print("\n\nResultat attendu : False")
    print("Test 1 : {}, obtenu : {}".format(LISTE_PAS_TRIEE1,est_triee(LISTE_PAS_TRIEE1)))
    print("Test 2 : {}, obtenu : {}".format(LISTE_PAS_TRIEE2,est_triee(LISTE_PAS_TRIEE2)))
    print("Test 3 : {}, obtenu : {}".format(LISTE_PAS_TRIEE2,est_triee(LISTE_PAS_TRIEE2)))

    if est_triee(LISTE_PAS_TRIEE3) or est_triee(LISTE_PAS_TRIEE2) or est_triee(LISTE_PAS_TRIEE3):
        fonction_valide = False

    # None ou Vide #
    print("Resultat attendu : False")
    print("Test : {}, obtenu : {}".format(LISTE_VIDE,est_triee(LISTE_VIDE)))

    if est_triee(LISTE_VIDE):
        fonction_valide = False

    return fonction_valide

#print(test_est_triee())

from Atelier3 import position_tri

def test_position_tri():
    """Test de la fonction position_tri"""
    print("TEST POSITION TRI")
    #Test liste vide
    print("Test liste vide")
    test = position_tri([], 0)
    if test == -1: #Résultat attendu : -1
        print("SUCCES : ", end='')
    else:
        print("ECHEC : ", end='')
    print("Attendu : -1 / Obtenu :", test)
    #Tests valeurs introuvable, au début, au milieu, à la fin
    lst = [-2, -1, 0, 3, 4, 6, 8]
    lst = sorted(lst) #Liste supposée triée
    e = [5, -2, 3, 8] #Liste des valeurs e
    resultats = [-1, 0, 3, 6] #Résultats attendus
    tests = ["introuvable", "au début", "au milieu", "à la fin"]
    for i in range(len(e)): #Boucle de tests
        print("Test valeur", tests[i])
        test = position_tri(lst, e[i])
        if test == resultats[i]:
            print("SUCCES : ", end='')
        else:
            print("ECHEC : ", end='')
        print("Attendu :", resultats[i], "/ Obtenu :", test)

test_position_tri()
'''

