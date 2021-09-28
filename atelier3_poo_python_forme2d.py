# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 14:33:22 2021

@author: notta
"""
from atelier3_poo_python_forme import Forme
import math

#abstract
class Forme2d(Forme):
    
    def __init__(self):
        super().__init__()
        
    def calcPerimetre():
        pass
    
    def __str__(self):
        return "Forme 2D {} et de perimetre: {}".format(super().__str__(),self.calcPerimetre())

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
    
    def __eq__(self, obj):
        res=False
        if isinstance(obj, Rectangle):
            if (obj.getLongueur()==self.__longueur and obj.getLargeur()==self.__largeur):
                res=True
        return res
    
    
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
    
    def __eq__(self, obj):
        res=False
        if isinstance(obj, Ellipse):
            if (obj.getDemiGrandAxe()==self._demiGrandAxe and obj.getdemiPetitAxe()==self._demiPetitAxe):
                res=True
        return res
    
class Cercle(Ellipse):
    
    def __init__(self, r):
        super().__init__(r, r)
        
    def getRayon(self):
        return self._demiGrandAxe
    
    def calcPerimetre(self):
        return 2*math.pi*self._demiGrandAxe
    
    def __eq__(self, obj):
        res=False
        if isinstance(obj, Cercle):
            if (obj.getRayon()==self._demiGrandAxe):
                res=True
        return res