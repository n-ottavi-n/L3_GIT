# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 13:36:42 2021

@author: notta
"""


#abstract
class Forme():
    
    numForme=0 #attribut statique
    
    def __init__(self):
        Forme.numForme+=1
        self.id_forme="_"+str(self.numForme)
        
    def calcSurface():
        pass
    
    def estLaplusGrande(self, forme):
        return (self.calcSurface()>forme.calcSurface())
    
    def __str__(self):
        return self.id_forme+" de surface: "+str(self.calcSurface())
    

    
    
        
        
        