# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 10:19:56 2021

@author: notta
"""
import numpy as np
import random as rd
import copy

objets = np.loadtxt("sacadot.txt", dtype=int)
Weight = 15

print(objets)
class individu():
    def __init__(self):
        self.genome = []
        self.price = 0
        self.weight = 0

    def fill_bag(self, not_in_bag = -1):
        selectable = [x for x in range(len(objets)) if objets[x,2] <= Weight - self.weight]
        if not_in_bag != -1:
            selectable.remove(not_in_bag) 
        while len(selectable) > 0:
            select = rd.choice(selectable)
            self.genome.append(select)
            self.price += objets[select, 1]
            self.weight += objets[select, 2]
            selectable.remove(select)
            LL = [x for x in selectable if objets[x,2] <= Weight - self.weight]
            selectable = LL

    def print(self):
        print(self.genome, end= " weight = " )
        print(self.weight, end= " price = ")
        print(self.price)


class population():
    def __init__(self, size, loop, precision):
        self.population_size = size
        self.max_loop = loop
        self.precision = precision
        self.individus = []
        self.max_price = []
        self.average = []

        for x in range(self.population_size):
            new_ind = individu()
            new_ind.fill_bag()
            self.individus.append(new_ind)
        self.max_price.append(max(self.individus, key=lambda individu: individu.price).price)
        self.average.append(sum(x.price for x in self.individus)/self.population_size)

    def mutation(self):
        for x in range(self.population_size):
            ind = copy.deepcopy(self.individus[x])
            select = rd.choice(ind.genome)
            ind.genome.remove(select)
            ind.price -= objets[select, 1]
            ind.weight -= objets[select, 2]
            ind.fill_bag()
            
    def reduce_population(self):
        self.individus=sorted(self.individus, key=lambda individu: individu.price, reverse=True)[:self.population_size]
        self.max_price.append(max(self.individus, key=lambda individu: individu.price).price)
        self.average.append(sum(x.price for x in self.individus)/self.population_size)


def genetic():    
    solution = population(5, 100, 0.001)
    for x in range(solution.max_loop):
        solution.mutation()
        solution.reduce_population()
    solution.individus[0].print()
    
genetic()