# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 15:39:25 2021

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

offset=0
TABLESYM=[]

def entrerSym(classe):
    global TABLESYM,offset
    TABLESYM+=[(PROGRAM[i-1],classe,offset)]
    offset+=1
    
def chercherSym(sym):
    global TABLESYM
    res=False
    for s in TABLESYM:
        if s[0]==sym:
            res=s
    if res:
        return res
    else:
        erreur_dec(sym)

length=len(PROGRAM)

def next_token():
    global i,token
    if i<(len(PROGRAM)-1):
        i+=1
        token=PROGRAM[i]
    
    
def erreur_dec(sym):
    print("variable {} not declared".format(sym))
    
def erreur(exp_token,given_token):
    print("ERREUR ", "expected: ",exp_token, " given: ",given_token)
    
def teste(test_token):
    #print('expected:',test_token,'given: ',token) 
    if test_token==token or re.match(test_token,token):
        next_token()
        return 1
    else:
        erreur(test_token, token)
        next_token()
        return 0
        
def test_et_entre(test_token, classe):
    if teste(test_token)==1:
        entrerSym(classe)
        
def test_et_cherche(test_token):
    tok=token
    if teste(test_token)==1:
        chercherSym(tok)
    
        
def consts():
    teste("const")       
    while token==ID:
        test_et_entre(ID,"constant")
        teste("==")
        teste(NUM)
        teste(";")
    

def Vars():
    teste("var")
    test_et_entre(ID,'variable')
    while token==",":
        next_token()
        test_et_entre(ID,'variable')
    teste(";")
    
def fact():
    if re.match(ID,token):
        test_et_cherche(ID)
    elif re.match(NUM, token):
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
    test_et_cherche(ID)
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
    test_et_cherche(ID)
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
    test_et_entre(ID, 'program')
    teste(";")
    block()
    if token != ".":
        erreur(".",token)
    
program()