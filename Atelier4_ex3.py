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
    """
    retourne une liste de mots

    Parameters
    ----------
    fileName : str
        fichier texte a convertir en liste

    Returns
    -------
    list
        liste de mots en minuscule et sans caracteres speciaux

    """
    capitals=[]
    file=open(fileName,"r",encoding=('utf8'))
    content=file.readlines()
    for line in content:
        capital=line.split("\t") #renvoie: [drapeau du pays pays, capitale]
        capital=line.partition("(")[0]#retire les termes entre parentheses
        capital=capital.strip("\n0123456789")#retire les nombres et les passages a la ligne
        capital=capital.partition("\t")[-1]#recupere ce qui apparait apres les tabulations
        capitals.append(capital)
    file.close()
    return capitals

#build_list("mots.txt")

import random

def runGame():
    """
    programme principal, lance le jeu du pendu

    Returns
    -------
    None.

    """

    #elements de la potence
    PENDU=["","|______","| / \\ ","|  T","|  O", "|----]"]
    #initialisations
    ind_pendu=0 #pour affichage de la potence    

    
    #choix difficultée    
    MOTS=build_list("mots.txt")
    MOTS_DICT=build_dict(MOTS) #creation du dictionnaire
    difficulte=int(input("Niveau de difficulté:\n(1.easy\n2.normal\n3.hard)"))
    if difficulte==1:
        mini,maxi=3,6
    elif difficulte==2:
        mini,maxi=7,8
    else:
        mini,maxi=9,30
        
    longueur=random.randint(mini, maxi)#init longueur
    #boucle jusqu'a avoir une longueur presente dans le dictionnaire
    while longueur not in MOTS_DICT.keys():
        longueur=random.randint(mini, maxi)
    mot=select_word(MOTS_DICT, longueur).lower()#choix du mot
    
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
        print(mot_out,"\n")
        #affichage du pendu
        for i in range(ind_pendu,0,-1):
            print(PENDU[i])
        res=mot_out.replace(" ","")#retrait des espaces pour comparer a mot
        #controle de la condition de victoire
        if res==mot:
            win=True
            msg_fin="gagné!"
            
    print(msg_fin)
    if not win:
        print(mot)
    
def build_dict(lst_m:list)->dict:
    """
    transforme une liste de mots en un dictionnaire de la forme {longueur mot: [liste de mots]}

    Parameters
    ----------
    lst_m : list
        liste de mots

    Returns
    -------
    dict
        dictionnaire {longueur mot:[liste mots]}

    """        
    mots_dict={}
    for mot in lst_m:
        if len(mot) not in mots_dict.keys():#si la cle n'existe pas dans le dictionnaire
            mots_dict.update({len(mot): [mot]})
        else:
            mots_dict[len(mot)].append(mot.strip())
    return mots_dict

MOTS=build_list("mots.txt")


MOTS_DICT=build_dict(MOTS)

def select_word(sorted_words:dict,word_len:int)->str:
    """
    selectionne un mot au hasard d'une longueur donnée

    Parameters
    ----------
    sorted_words : dict
        dictionnaire de la forme {longueur mot: [liste mots]}
    word_len : int
        longueur du mot desiré

    Returns
    -------
    str
        mot de la bonne taille choisi au hasard

    """
    lst_mots=sorted_words[word_len] #liste de mots de taille word_len
    randint=random.randint(0, len(lst_mots)-1) #int aleatoir entre 0 et taille liste
    return lst_mots[randint]



runGame()    

