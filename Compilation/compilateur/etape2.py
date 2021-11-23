# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 13:44:16 2021

@author: notta
"""

import re

TOKENS=["program","ID",";","CONSTS","var","INSTS","begin","end"]
i=0 #indice du token actuel
token=TOKENS[0]
ID='[a-zA-Z]+[0-9]*'
NUM='[0-9]+'

PROGRAM=["program",'abc',';','var','A',',','B',';',
         'begin',
         #'A',':=','0',';',
         #'B',':=','0',';',
         'while','A','<>','0','do',
         'begin',
         'read','(','A',')',';',
         'B',':=','A','+','B',';',
         'end',
         'write','(','B',')',';',         
         'end','.']

def next_token():
    global i,token
    i+=1
    token=PROGRAM[i]
    
    

def erreur(token):
    print("ERREUR ",token)
    
def teste(token):
    print('expected:',token,'given: ',PROGRAM[i])
 
    if token==PROGRAM[i] or re.match(token,PROGRAM[i]):
        next_token()
        return 1
    else:
        erreur(token)
        next_token()
        
def consts(token):
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
    
def fact(token):
    if re.match(ID,token) or re.match(NUM, token):
        next_token()
    else:
        teste("(")
        expr(token)
        teste(")")
    
def term(token):
    fact(token)
    while token in ["*","/"]:
        next_token()
        fact(token)
    
def expr(token):
    term(token)
    print("expr_token: ",token)
    while token in ["+","-"]:
        next_token()
        term(token)

def cond(token):
    expr(token)
    if token in ["==","<>","<",">","<=",">="]:
        next_token()
        expr(token)
    
def affec(token):
    teste(ID)
    teste(":=")
    expr(token)

def si(token):
    teste("if")
    cond(token)
    teste("then")
    inst(token)

def tantQue(token):
    teste("while")
    cond(token)
    teste("do")
    inst(token)

def ecrire(token):
    teste("write")
    teste("(")
    expr(token)
    while token==",":
        next_token()
        expr(token)
    teste(")")

def lire(token):
    teste("read")
    teste("(")
    teste(ID)
    while token==",":
        next_token()
        teste(ID)
    teste(")")

def insts(tokenA):
    global token
    teste("begin")
    inst(token)  
    while token==";":
        next_token()
        print("insts:",token)
        inst(token)
    teste("end")
    
def inst(token):
    
    if token=="if":
        si(token)
    elif token=="while":
        tantQue(token)
    elif token=="begin":
        insts(token)
    elif token=="write":
        ecrire(token)
    elif token=="read":
        lire(token)
    elif re.match(ID,token):
        affec(token)

        
def block(token):
    if token=="const":
        consts(token)
    elif token=="var":
        Vars()
    insts(token)
    
def program(TOKENS):
    teste("program")
    teste(ID)
    teste(";")
    block(token)
    
program(TOKENS)






    