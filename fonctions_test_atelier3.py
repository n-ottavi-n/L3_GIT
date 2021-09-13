# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 13:46:46 2021

@author: notta
"""
from Atelier3 import separer

def test_separer():
    """teste la fonction separer()"""
    #test liste vide
    LST=[]
    test=separer(LST)
    attendu=[]
    
    print("attendu: {}\nresultat: {}".format(attendu,test))  
    print(attendu==test)
    
    #test liste normal, 
    LST=[-1,2,-12,0,4,0,5,-6]
    test=separer(LST)
    attendu=[-1, -12, -6, 0, 0, 5, 4, 2]
    
    print("attendu: {} \nresultat: {}".format(attendu,test))    
    print(attendu==test)
    
    #test liste entiers positifs, 
    LST=[1,2,3]
    test=separer(LST)
    attendu=[3,2,1]
    
    print("attendu: {}\nresultat: {}".format(attendu,test))
    print(attendu==test)
    
    #test lsite de 0
    LST=[0,0,0,0]
    test=separer(LST)
    attendu=[0,0,0,0]
    
    print("attendu: {}\nresultat: {}".format(attendu,test))
    print(attendu==test)
    
    
test_separer()