# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 10:49:11 2021

@author: notta
"""
import random

def plusoumoins(min:int,max:int):
    randomNumber=random.randint(min,max)
    finDuJeu=False
    coup=1
    while not(finDuJeu) and (coup<11):
        monNbr=int(input("Entrez un nombre: "))
        if(monNbr>randomNumber):
            print("trop grand")
        elif(monNbr<randomNumber):
            print("trop petit")
        else:
            print("Tu gagnes en ",coup," coup(s)")
            finDuJeu=True
        coup+=1
    if(coup>10):
        print("perdu")
        
plusoumoins(0, 10)
        