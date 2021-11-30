# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 13:44:16 2021

@author: notta
"""

import re

TOKENS=["program","begin","end","read","write","if","while","(",")"]
i=0 #indice du token actuel
ID='[a-zA-Z][a-zA-Z_0-9]*'
NUM='[0-9]+'

PROGRAM=["program",'abc',';','var','A',',','B',';',
         'begin',
         'A',':=','0',';',
         'B',':=','0',';',
         'while','A','<>','0','do',
         'begin',
         'read','(','A',')',';',
         'B',':=','A','+','B',';',
         'end',';',
         "write",'(','B',')',';', 
         'end','.']

token=PROGRAM[0]

length=len(PROGRAM)

def next_token():
    global i,token
    if i<(len(PROGRAM)-1):
        i+=1
        token=PROGRAM[i]
    
    

def erreur(exp_token,given_token):
    print("ERREUR ", "expected: ",exp_token, " given: ",given_token)
    
def teste(test_token):
    print('expected:',test_token,'given: ',token) 
    if test_token==token or re.match(test_token,token):
        next_token()
        return 1
    else:
        erreur(test_token, token)
        next_token()
        
def consts():
    teste("const")   
    while token==ID:
        teste(ID)
        teste("==")
        teste(NUM)
        teste(";")
    

def Vars():
    teste("var")
    teste(ID)
    while token==",":
        next_token()
        teste(ID)
    teste(";")
    
def fact():
    if re.match(ID,token) or re.match(NUM, token):
        next_token()
    else:
        teste("(")
        expr()
        teste(")")
    
def term():
    fact()
    while token in ["*","/"]:
        next_token()
        fact()
    
def expr():
    #print("expr_token: ",token)
    term()
    while token in ["+","-"]:
        next_token()
        term()

def cond():
    expr()
    if token in ["==","<>","<",">","<=",">="]:
        next_token()
        expr()
    
def affec():
    teste(ID)
    teste(":=")
    expr()

def si():
    teste("if")
    cond()
    teste("then")
    inst()

def tantQue():
    teste("while")
    cond()
    teste("do")
    inst()

def ecrire():
    teste("write")
    teste("(")
    expr()
    while token==",":
        next_token()
        expr()
    teste(")")

def lire():
    teste("read")
    teste("(")
    teste(ID)
    while token==",":
        next_token()
        teste(ID)
    teste(")")

def insts():
    teste("begin")
    inst()  
    while token==";":
        next_token()
        #print("insts:",token)
        inst()
    teste("end")
    
def inst():   
    print("inst: ",token)
    if token=="if":
        si()
    elif token=="while":
        tantQue()
    elif token=="begin":
        insts()
    elif token=="write":
        ecrire()
    elif token=="read":
        lire()
    elif re.match(ID,token) and token not in TOKENS:        
        affec()

        
def block():
    if token=="const":
        consts()
    elif token=="var":
        Vars()
    insts()
    
def program():
    teste("program")
    teste(ID)
    teste(";")
    block()
    if token != ".":
        erreur(".",token)
    
program()






    