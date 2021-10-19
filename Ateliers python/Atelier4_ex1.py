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
    str_arg=str_arg.strip()
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

def is_mail(str_arg:str)->(int,int):
    """teste la validite de l'adresse mail passée en parametre, renvoie un tuple
    avec resultat du test et code d'erreur'

    Parameters
    ----------
    str_arg : str
        adresse mail

    Returns
    -------
    (int,int)
        tuple de la forme(validite(valide: 1, 0 sinon), code erreur) 
        codes erreur:
            0, pas d'erreur
            1,corps non valide
            2, @ manquante
            3,domaine non valide
            4 "." absent

    """
    valide=1
    code_err=0
    termine=False
    partition=str_arg.rpartition("@")#renvoie: (corps,@,nom de domaine.suffixe)
    while valide==1 and not termine :
        if partition[1]=='':# @ absente
            valide=0
            code_err=2
        else:
            corps=partition[0]
            if corps=='':
                valide=0
                code_err=1
            partition2=partition[2].rpartition(".")#renvoie: (nom_domaine, ., suffixe)
            if partition2[1]=='': # "." absent
                valide=0
                code_err=4
            else:
                nom_domaine=partition2[0]
                suffixe=partition2[2]
                partition3=nom_domaine.rpartition("-")#renvoie: (univ, -, corse)
                if nom_domaine=='' or suffixe=='' or partition3[1]=='' : #pas de nom de domaine ou de suffixe ou de "-"
                    valide=0
                    code_err=3
            termine=True
    return (valide,code_err)

#print(is_mail("nottavi14@gmailcom"))


                    
                    
            
            
                
            
        
    
        
    
        

    
    
    
    