# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 08:39:10 2021

@author: notta
"""

import random

donnees=[[2,4,8,3,5,1,3,13,5,6,7,11],[5,7,2,2,6,8,3,4,9,11,8,7]] #[[prix],[poids]]

        
        

def algoGenetique(donnees, poidMax):   
    lstPoids=donnees[1]
    lstPrix=donnees[0]
    long=len(lstPrix) #longueur des listes
    poid=0
    prix=0
    ind=0
    genome=[]
    
    #premier genome
    while ind<long:
        x=random.randint(0,1)
        if x>0.5 and poid+lstPoids[ind]<=poidMax:
            poid+=lstPoids[ind]
            prix+=lstPrix[ind]
            genome+=[1]
        else:
            genome+=[0]
        ind+=1
        
    #algo evolution
    prixBest=prix
    for i in range(1000): #on fait 200 iterations    
        print("prix: ",prix)
        valeurGenome=0
        newGenome=genome.copy()   
        poid=0
        prix=0
        #on additionne les poids et prix
        for j in range(len(genome)):
            poid+=lstPoids[j]*newGenome[j]
            prix+=lstPrix[j]*newGenome[j]
        newGenome=genome.copy()
        valeurGenome=0        
        y=0
        #on enleve un gene au hasard
        while valeurGenome==0:#on cherche un 1 dans la liste au hasard
            y=random.randrange(0,long)#indice pris au hasard, la case doit valoir 0
            valeurGenome=newGenome[y]
        newGenome[y]=0 #le 1 devient 0        
        #maj des poids et des prix
        poid-=lstPoids[y]
        prix-=lstPrix[y]       
        
        #on choisit un nouveau gene
        nouvelleValeurGenome=1 #le nouveau gene doit etre un 0
        z=0
        while nouvelleValeurGenome==1:      
            z=random.randrange(0,long) #indice pris au hasard, la case doit valoir 1
            if poid+lstPoids[z]<=poidMax:
                nouvelleValeurGenome=newGenome[z]
                newGenome[z]=1 #le 0 devient 1
                #maj des poids et des prix
        poid+=lstPoids[z]
        prix+=lstPrix[z]
        
        
        if prix>prixBest: #mise a  jour de la meilleur solution
            prixBest=prix
            genome=newGenome    
            print("changement")
                 
    return genome,prix,poid

res=algoGenetique(donnees, 15)
print("{} prix: {}, poid: {}".format(res[0],res[1],res[2]))
        