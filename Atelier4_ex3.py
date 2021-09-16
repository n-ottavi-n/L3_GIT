# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 08:44:01 2021

@author: notta
"""

def places_lettre(ch:str,mot:str)->list:
    """
    cherche le caractere 'ch' dans la string 'mot' et renvoie une liste des indices 
    renvoie une liste vide si 'ch' absent

    Parameters
    ----------
    ch : str
        caractere a chercher
    mot : str
        mot dans lequel la recherche est effectuée

    Returns
    -------
    list
        liste des indices de ch dans mot, liste vide si ch absent

    """
    res=[]
    for i in range(len(mot)):
        if mot[i]==ch:
            res.append(i)
    return res

def outputStr(mot:str,lpos:list)->str:
    """
    renvoie une chaine de caractere contenant le mot avec 0 ou plusieurs caracteres remplacés
    par des "_"

    Parameters
    ----------
    mot : str
        mot a afficher
    lpos : list
        liste d'entiers representant les indices des caracteres du mot a afficher'

    Returns
    -------
    str
        le mot avec 0 ou plusieurs caracteres remplacés par des "_"

    """
    mot_out=""
    for i in range(len(mot)):
        if i in lpos:
            mot_out+=mot[i]+" "
        else:
            mot_out+="_ "
    return mot_out

def build_list(fileName:str)->list:
    file=open(fileName,"r")
    content=file.readlines()
    print(content)
    file.close()

build_list("mots.txt")

import random

def runGame():
    """
    programme principal, lance le jeu du pendu

    Returns
    -------
    None.

    """
    #liste de mots
    MOTS=["bonjour","demain","bientot","matin","universite","pandemie","soleil","tableau",
          "bouteille"]
    #elements de la potence
    PENDU=["","|______","| / \\ ","|  T","|  O", "|----]"]
    #initialisations
    ind_pendu=0 #pour affichage de la potence    
    rd_int=random.randint(0,len(MOTS)-1)#choisit un entier aleatoire
    mot=MOTS[rd_int]#selection aleatoire du mot    
    lpos=[]
    
    print(outputStr(mot, lpos))#affiche "_ _ _ _ _ _"
    
    win=False
    erreurs=0
    msg_fin="perdu :("
    #boucle principale, saisie des lettre, mise a jour des erreurs et affichage de l'avancement,
    #controle de la condition de victoire
    while not win and erreurs<5:
        print(erreurs, "erreur(s)")
        lettre=input("entrez une lettre: ")
        new_lettre_pos=places_lettre(lettre, mot)
        if not new_lettre_pos:#la lettre n'est pas dans le mot, +1 erreur,
            erreurs+=1
            ind_pendu+=1 #on rajoute un element a la potence            
        lpos+=(new_lettre_pos)#mise a jour des lettres révélées
        mot_out=outputStr(mot, lpos)#mise a jour du mot avec le nouveau lpos
        print(mot_out)
        #affichage du pendu
        for i in range(ind_pendu,0,-1):
            print(PENDU[i])
        res=mot_out.replace(" ","")#retrait des espaces pour comparer a mot
        #controle de la condition de victoire
        if res==mot:
            win=True
            msg_fin="gagné!"
            
    print(msg_fin)
        
    

#runGame()    

