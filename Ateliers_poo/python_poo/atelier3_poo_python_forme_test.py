# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 15:35:23 2021

@author: notta
"""
from atelier3_poo_python_forme import Forme
from atelier3_poo_python_forme2d import *
from atelier3_poo_python_forme3d import *



s1=Sphere(2)
print(s1)
s2=Sphere(2)
s3=Sphere(3)
print(s1.__eq__(s2))
print(s2.__eq__(s3))

c1=Cercle(1)
print(c1)
c2=Cercle(1)
c3=Cercle(3)
print(c1.__eq__(c2))
print(c2.__eq__(c3))