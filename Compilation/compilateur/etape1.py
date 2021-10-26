# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 13:43:59 2021

@author: notta
"""
MEM=[0,1,2] #pile d'entiers
SP=0 #pointeur de pile
P_CODE=[] #tableau d'instructions
PC=0 #pointeur d'instructions
INST=""#instruction en cours
end=False

def add(pile):
    res=pile[-1]+pile[-2]
    del pile[-1]
    pile[-1]=res
    
def sub(pile):
    res=pile[-1]-pile[-2]
    del pile[-1]
    pile[-1]=res
    
def mul(pile):
    res=pile[-1]*pile[-2]
    del pile[-1]
    pile[-1]=res
    
def div(pile):
    res=pile[-1]//pile[-2]
    del pile[-1]
    pile[-1]=res
    
def eql(pile):
    res=(pile[-1]==pile[-2])
    del pile[-1]
    pile[-1]=int(res)
    
def neq(pile):
    res=(pile[-1]!=pile[-2])
    del pile[-1]
    pile[-1]=int(res)
    
def gtr(pile):
    res=(pile[-1]>pile[-2])
    del pile[-1]
    pile[-1]=int(res)
    
def lss(pile):
    res=(pile[-1]<pile[-2])
    del pile[-1]
    pile[-1]=int(res)
    
def geq(pile):
    res=(pile[-1]>=pile[-2])
    del pile[-1]
    pile[-1]=int(res)
    
def leq(pile):
    res=(pile[-1]<=pile[-2])
    del pile[-1]
    pile[-1]=int(res)
    
def prn(pile):
    res=pile[-1]
    del pile[-1]
    print(res)
    
def inn(pile):
    a=input()
    adresse=pile[-1]
    pile[adresse]=a
    del pile[-1]
    
def int_c(SP,c):
    SP+=c
    
def ldi(pile,v):
    pile+=[v]
    
def lda(pile,a):
    pile+=[a]
    
def ldv(pile):
    adresse=pile[-1]
    pile[-1]=pile[adresse]
    
def sto(pile):
    adresse=pile[-2]
    pile[adresse]=pile[-1]
    del pile[-1]
    del pile[-1]
    
def brn(i,PC):
    global PC
    PC=i
    
def bze(i,pile):
    if pile[-1]==0:
        brn(i)
    del pile[-1]
    
def hlt(ps):
    ps="END"
    
MNEMONIQUES=["ADD","SUB","MUL","DIV","EQL","NEQ","GTR","LSS","GEQ",
             "LEQ","PRN","INN","INT","LDI","LDA","LDV","STO","BRN",
             "BZE","HLT"]
    
def interpreteur(PCODE):
    MEM=[]
    SP=0 #pointeur de pile
    PC=0 #pointeur d'instructions
    PS="EXECUTION" #program status
    INST=""#instruction en cours
    for i in range(len(PCODE)):
        INST=PCODE[PC]        
        PC+=1
        switch (INST){
            case "ADD": add(MEM);
            }
        
            
        

    
    
    
print(MEM)
ldi(MEM,3)
print(MEM)
    

    






