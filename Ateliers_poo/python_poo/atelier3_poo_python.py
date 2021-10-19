# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 13:36:42 2021

@author: notta
"""

from abc import ABC, abstractmethod
import math

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
    
class Forme2d(Forme):
    
    def __init__(self):
        super().__init__()
        
    def calcPerimetre():
        pass
    
class Rectangle(Forme2d):
    
    def __init__(self, a, b):
        super().__init__()
        self.__longueur=a #attribut privé
        self.__largeur=b #attribut privé
        
    def getLongueur(self):
        return self.__longueur
    
    def getLargeur(self):
        return self.__largeur
    
    def calcPerimetre(self):
        return 2*(self.__longueur+self.__largeur)
    
    def calcSurface(self):
        return self.__longueur*self.__largeur
    
    
class Ellipse(Forme2d):
    
    def __init__(self, a, b):
        super().__init__()
        self._demiGrandAxe=a #attribut privé
        self._demiPetitAxe=b #attribut privé
        
    def getDemiGrandAxe(self):
        return self._demiGrandAxe
    
    def getDemiPetitAxe(self):
        return self._demiPetitAxe
    
    def calcPerimetre(self):
        return math.pi*math.sqrt(2*((self._demiGrandAxe**2)+(self._demiPetitAxe**2)))
    
    def calcSurface(self):
        return math.pi*self._demiGrandAxe*self._demiPetitAxe
    
class Cercle(Ellipse):
    
    def __init__(self, r):
        super().__init__(r, r)
        
    def getRayon(self):
        return self._demiGrandAxe
    
    def calcPerimetre(self):
        return 2*math.pi*self._demiGrandAxe
    
    
#e1=Ellipse(5,3)
#print(e1.calcPerimetre())
c1=Cercle(5)
print(c1.getRayon())
    
    
        
    
    
        
        
        