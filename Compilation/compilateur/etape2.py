# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 13:44:16 2021

@author: notta
"""

TOKENS=["program","id",";","BLOCK"]

i=0

def erreur(token):
    print("ERREUR ",token)
    
def teste(token,next_token):
    if next_token==token:
        return 1
    else:
        erreur(token)
    
def program(TOKENS):
    i=0
    token=TOKENS[i]
    i+=1
    teste(token,"program")
    token=TOKENS[i]
    i+=1
    teste(token,"id")
    token=TOKENS[i]
    i+=1
    teste(token,";")
    token=TOKENS[i]
    i+=1
    
program(TOKENS)
    