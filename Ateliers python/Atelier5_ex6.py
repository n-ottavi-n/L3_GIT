# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 20:19:02 2021

@author: notta
"""

def sort_list(lst_a_trier:list)->list:
    """
    Retourne une liste triée dans l'ordre croissant

    Parameters
    ----------
    lst_a_trier : list
        liste d'entiers'

    Returns
    -------
    list
        liste triée

    """
    lst_triee=lst_a_trier.copy()
    for i in range(len(lst_triee)-1):
        if lst_triee[i+1]<lst_triee[i]:#si case suivante<case actuelle
            lst_triee[i],lst_triee[i+1]=lst_triee[i+1],lst_triee[i]#echange des cases
    return lst_triee
        

lst_test=[5,2,3,7,9]

#print(sort_list(lst_test))

import time
import matplotlib.pyplot as plt
from Atelier5_ex1 import gen_list_random_int

def perf_sort(taille_des_listes:list,iterations:int)->tuple:
    """
    compare les performances de sort_list(fonction1) 
    et sorted(fonction2)

    Parameters
    ----------

    taille_des_listes : list
        taille des listes sur lequelles les tests seront effectues
    iterations : int
        nombre d'iterations par test pour obtenir une moyenne

    Returns
    -------
    tuple de 2 listes
        ([temps d'execution moyen fonction1],[temps d'execution moyen fonction2])

    """
    res=()
    lst_perf_f1=[]
    lst_perf_f2=[]
    
    for len_list in taille_des_listes:#une taille de liste apres l'autre
        print("liste en cours ", len_list)
        moyenne_f1=0 #moyenne sur la fonction 1
        moyenne_f2=0 #----------------------- 2
        #genere une liste aleatoire de taille len_list -configuration1, default
        test_list=gen_list_random_int(len_list)
        #conf=1
        #configuration2, liste triee
        #test_list=sorted(test_list)
        #conf=2
        #configuration3, liste inversement triee
        test_list=sorted(test_list,reverse=True)
        conf=3
        for iteration in range(iterations):
            #test fonction1
            start_pc = time.perf_counter()#debut horloge
            sort_list(test_list)#test fonction1
            end_pc = time.perf_counter()#fin horloge
            duree=end_pc-start_pc #resultat du test
            moyenne_f1+=duree
            #test fonction2
            start_pc = time.perf_counter()#debut horloge
            sorted(test_list)#test fonction2
            end_pc = time.perf_counter()#fin horloge
            duree=end_pc-start_pc
            moyenne_f2+=duree
        moyenne_f1=moyenne_f1/iterations #calcul de la moyenne1
        lst_perf_f1.append(moyenne_f1) #ajout de la moyenne 1
        moyenne_f2=moyenne_f2/iterations
        lst_perf_f2.append(moyenne_f2)
    res+=(lst_perf_f1,lst_perf_f2)#ajout des resultats dans le tuple de sortie
    #matplotlib
    fig, ax = plt.subplots()
    ax.plot(taille_des_listes,lst_perf_f1, 'r*-', label='sort_list')
    ax.plot(taille_des_listes,lst_perf_f2,'g*-', label='sorted')
    ax.set(xlabel='taille de liste', ylabel='temps execution',
    title='sort_list et sorted conf{}'.format(conf))
    ax.legend(loc='upper center', shadow=True, fontsize='x-large')
    #fig.savefig("test.png")
    plt.show()
    return res

taille_lst=[10, 50, 100, 500, 1000, 5000, 10000]
iterations=100

print(perf_sort(taille_lst, iterations))