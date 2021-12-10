# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 09:14:36 2021

@author: notta
"""

mot1='detentes'
mot2='distances'



def plss(mot1,mot2):
    tab=[]
    for i in range(len(mot1)+1):
        tab.append([0]*(len(mot2)+1))
    for i in range(1,len(mot1)+1):
        for j in range(1,len(mot2)+1):            
                val=[tab[i-1][j]]
                val.append(tab[i][j-1])
                val.append(tab[i-1][j-1]+(1 if mot1[i-1]==mot2[j-1] else 0))
                tab[i][j]=max(val)
    for i in range(len(mot1)+1):
        print(tab[i])
    return tab

tab=[]
for i in range(len(mot1)+1):
    tab.append(['-']*(len(mot2)+1))

    
def plssRecursive(mot1,mot2):
    if len(mot1)==0: 
        tab[len(mot1)][len(mot2)]=0
        return 0
    if len(mot2)==0: 
        tab[len(mot1)][len(mot2)]=0
        return 0
    val=[plssRecursive(mot1[0:-1],mot2)]
    val.append(plssRecursive(mot1,mot2[0:-1]))
    val1=plssRecursive(mot1[0:-1],mot2[0:-1])+(1 if mot1[-1]==mot2[-1] else 0)
    val2=plssRecursive(mot1[0:-1],mot2)
    if val1!=val2:
        tab[len(mot1)][len(mot2)]=max(val1,val2)
        return max(val1,val2)
    val2=plssRecursive(mot1,mot2[0:-1])
    tab[len(mot1)][len(mot2)]=max(val1,val2)
    return(max(val))


print(plssRecursive(mot1,mot2))

