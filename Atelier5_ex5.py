# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 20:19:02 2021

@author: notta
"""

import random

import time
"""
#Pour mesurer le temps d'exécution nous avons à notre disposition
#la fonction perf_counter()
n = 10000000
#Récupération du temps système et démarrage du chronomètre
start_pc = time.perf_counter()
for i in range(n):
 #on ne fait rien…
 None
end_pc = time.perf_counter()
elapsed_time_pc = end_pc-start_pc
print("Temps écoulé entre les deux mesures : ",elapsed_time_pc)
print("Temps estimé pour une instruction",elapsed_time_pc/n)
# Exécutez ce code et vérifiez par vous-même la variabilité des mesures.

import matplotlib.pyplot as plt
import numpy as np
#Ici on décrit les abscisses
#Entre 0 et 5 en 10 points
x_axis_list = np.arange(0,5.5,0.5)
fig, ax = plt.subplots()
#Dessin des courbes, le premier paramètre
#correspond aux point d'abscisse le
#deuxième correspond aux points d'ordonnées
#le troisième paramètre, optionnel permet de
#choisir éventuellement la couleur et le marqueur
ax.plot(x_axis_list,x_axis_list,'bo-',label='Identité')
ax.plot(x_axis_list,x_axis_list**2, 'r*-', label='Carré')
ax.plot(x_axis_list,x_axis_list**3,'g*-', label='Cube')
ax.set(xlabel='Abscisse x', ylabel='Ordonnée y',
 title='Fonctions identité, cube et carré')
ax.legend(loc='upper center', shadow=True, fontsize='x-large')
#fig.savefig("test.png")
plt.show()
"""
import matplotlib.pyplot as plt

from Atelier5_ex2 import mix_list
from Atelier5_ex1 import gen_list_random_int

def perf_mix(taille_des_listes:list,iterations:int)->tuple:
    """
    compare les performances de mix_list(fonction1) et random.shuffle(fonction2)

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
        test_list=gen_list_random_int(0,len_list)#genere une liste aleatoire de taille len_list
        for iteration in range(iterations):
            #test fonction1
            start_pc = time.perf_counter()#debut horloge
            mix_list(test_list)#test
            end_pc = time.perf_counter()#fin horloge
            duree=end_pc-start_pc #resultat du test
            moyenne_f1+=duree
            #test fonction2
            start_pc = time.perf_counter()#debut horloge
            random.shuffle(test_list)#test
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
    ax.plot(taille_des_listes,lst_perf_f1, 'r*-', label='mix_list')
    ax.plot(taille_des_listes,lst_perf_f2,'g*-', label='shuffle')
    ax.set(xlabel='taille de liste', ylabel='temps execution',
     title='Fonctions identité, mix_list et shuffle')
    ax.legend(loc='upper center', shadow=True, fontsize='x-large')
    #fig.savefig("test.png")
    plt.show()
    return res


taille_lst=[10, 50, 100, 500, 1000]
iterations=10

#print(perf_mix(taille_lst, iterations))

from Atelier5_ex4 import extract_element_list

def perf_extract(taille_des_listes:list,iterations:int)->tuple:
    """
    compare les performances de extract_element_list(fonction1) 
    et random.sample(fonction2)

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
        test_list=gen_list_random_int(0,len_list)#genere une liste aleatoire de taille len_list
        for iteration in range(iterations):
            #test fonction1
            start_pc = time.perf_counter()#debut horloge
            extract_element_list(test_list,5)#test fonction1
            end_pc = time.perf_counter()#fin horloge
            duree=end_pc-start_pc #resultat du test
            moyenne_f1+=duree
            #test fonction2
            start_pc = time.perf_counter()#debut horloge
            random.sample(test_list,5)#test fonction2
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
    ax.plot(taille_des_listes,lst_perf_f1, 'r*-', label='extract_element_list')
    ax.plot(taille_des_listes,lst_perf_f2,'g*-', label='random.sample')
    ax.set(xlabel='taille de liste', ylabel='temps execution',
     title='extract_element_list et random.sample')
    ax.legend(loc='upper center', shadow=True, fontsize='x-large')
    #fig.savefig("test.png")
    plt.show()
    return res


taille_lst=[10, 50, 100, 500, 1000, 5000, 10000]
iterations=10000

print(perf_extract(taille_lst, iterations))
     
       
            
        
    
