# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 11:36:47 2021

@author: notta
"""

def full_name(str_arg:str)->str:
    """
    renvoie une chaine de caractere au format 'NOM Prenom'

    Parameters
    ----------
    str_arg : str
        nom entré au format 'nom prenom'

    Returns
    -------
    str
        nom correctement formaté

    """
    lettre=str_arg[0]
    res=""#nouvelle string
    i=0
    while lettre!=' ':#boucle jusq'a atteindre l'espace
        res+=lettre.upper()#ajout des majuscules une par une
        i+=1
        lettre=str_arg[i]
    #i=indice de l'espace
    res+=str_arg[i]#ajout de l'espace
    lettre=str_arg[i+1]# recupere la premiere lettre du prenom
    res+=lettre.upper()#premiere lettre du prenom pass en majuscule
    res+=str_arg[i+2:]#ajout du reste d ela string d'entree
    return res

nom="ottavi nicolas"
print(full_name(nom))


    
    
    
    