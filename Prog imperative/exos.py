# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 11:08:13 2021

@author: notta
"""

import random

##############1###################

def somme(n):
    if n==1:
        return 1
    else:
        return n+somme(n-1)
    
#print(somme(5))

################5###############

def fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
'''
for i in range(10):
    print(fibo(i))'''
    
##################3################

def puiss(x,n):
    if n==1:
        return x
    else:
        return x*puiss(x,n-1)
    
#print(puiss(2,10))

###########

###############4#############

lst=random.sample(range(0,5000), 10)
n=random.randrange(0,5000)

def plusProche(n,lst):
    print(n)
    
#plusProche(n,lst)
    
########2########

def contientZero(n):
    print(n)
    if n<10:
        return n==0
    elif n%10==0:
        return True
    else:
        contientZero(n//10)
    

#print(contientZero(1024))


#######4#######

def distance(x,d,f,t):
    if d==f:
        return abs(x-t[0])
    else:
        return min(abs(x-t[0]),distance(x,d+1,f,t))
    
lst=random.sample(range(0,50), 10)
n=random.randrange(0,50)

print(lst)
print(n)
print(distance(n,0,len(lst)-1,lst))


        
        
        
        
        

        
    
    
    
    