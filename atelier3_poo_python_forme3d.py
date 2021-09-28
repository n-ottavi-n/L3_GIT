# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 14:36:33 2021

@author: notta
"""
from atelier3_poo_python_forme import Forme
import math

#abstract
class Forme3d(Forme):
    
    def __init__(self):
        super().__init__()
        
    def calcVolume():
        pass
    
    def __str__(self):
        return "Forme 3D "+super().__str__()+" et de volume: "+str(self.calcVolume())
    
class Cylindre(Forme3d):
    
    def __init__(self,r,h):
        super().__init__()
        self.__rayon=r
        self.__hauteur=h
        
    def getRayon(self):
        return self.__rayon
    
    def getHauteur(self):
        return self.__hauteur
    
    def calcVolume(self):
        return self.__hauteur*(math.pi*(self.__rayon**2))
    
    def calcSurface(self):
        return (2*math.pi*self.__rayon*self.__hauteur)+2*(math.pi*(self.__rayon**2))
    
    def __eq__(self, obj):
        res=False
        if isinstance(obj, Cylindre):
            if (obj.getRayon()==self.__rayon and obj.getHauteur()==self.__hauteur):
                res=True
        return res
    
class Sphere(Forme3d):
    
    def __init__(self,r):
        super().__init__()
        self.__rayon=r
             
    def getRayon(self):
        return self.__rayon
    
    def calcVolume(self):
        return (4/3)*math.pi*(self.__rayon**3)
    
    def calcSurface(self):
        return 4*math.pi*(self.__rayon**2)
    
    def __eq__(self, obj):
        res=False
        if isinstance(obj, Sphere):
            if (obj.getRayon()==self.__rayon):
                res=True
        return res
        

        
        