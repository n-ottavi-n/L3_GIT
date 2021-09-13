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
    test1=(attendu==test)
    
    print("attendu: {}\nresultat: {}".format(attendu,test))  
    print(test1,"\n-------")
    
    #test liste normal, 
    LST=[-1,2,-12,0,4,0,5,-6]
    test=separer(LST)
    attendu=[-1, -12, -6, 0, 0, 5, 4, 2]
    test2=(attendu==test)
    
    print("attendu: {} \nresultat: {}".format(attendu,test))    
    print(test2,"\n-------")
    
    #test liste entiers positifs, 
    LST=[1,2,3]
    test=separer(LST)
    attendu=[3,2,1]
    test3=(attendu==test)
    
    print("attendu: {}\nresultat: {}".format(attendu,test))
    print(test3,"\n-------")
    
    #test lsite de 0
    LST=[0,0,0,0]
    test=separer(LST)
    attendu=[0,0,0,0]
    test4=(attendu==test)
    
    print("attendu: {}\nresultat: {}".format(attendu,test))
    print(test4,"\n-------")
    
    if test1 and test2 and test3 and test4:
        res="#####SUCCES#####"
    print(res)
    
    
test_separer()