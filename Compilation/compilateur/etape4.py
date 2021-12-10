# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 14:42:46 2021

@author: notta
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 15:39:25 2021

@author: notta
"""
import re

TOKENS=["program","begin","end","read","write","if","while","(",")","var"]
i=0 #indice du token actuel
ID='[a-zA-Z][a-zA-Z_0-9]*'
NUM='[0-9]+'

PROGRAM=["program",'abc',';',
         'var','A',',','B',';',
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

def next_inst(compt):
    return False

def getAdresseFromTableSym(nomVar):
    ADDR=0
    for dec in TABLESYM:
        if dec[0]==nomVar:
            ADDR=dec[2]
    return ADDR

def entrerSym(classe,value):
    global TABLESYM,offset
    if classe=='constant':
        value=PROGRAM[i+1]
    TABLESYM+=[(PROGRAM[i-1],classe,value)]
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
    global offset
    if teste(test_token)==1:
        entrerSym(classe,value=offset)
        
def test_et_cherche(test_token):
    tok=token
    if teste(test_token)==1:
        chercherSym(tok)
    
        
def consts():
    teste("const")       
    while re.match(ID,token) and token!='var':
        test_et_entre(ID,"constant")
        teste("=")
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
        nomVar=token
        test_et_cherche(ID)
        for line in TABLESYM:
            if line[1]=='constant':
                generer2('LDI',TABLESYM.index(line))
            if line[1]=='variable':
                generer2('LDA',getAdresseFromTableSym(nomVar))
                generer1('LDV')
    elif re.match(NUM, token):
        generer2('LDI',token)
        next_token()
        
    else:
        teste("(")
        expr()
        teste(")")
    
def term():
    global token
    fact()
    while token in ["*","/"]:
        op=token
        next_token()
        fact()
        if op=="*":
            generer1('MUL')
        else:
            generer1('DIV')
    
def expr():
    global token
    #print("expr_token: ",token)
    term()
    while token in ["+","-"]:
        op=token
        next_token()
        term()
        if op=="+":
            generer1('ADD')
        else:
            generer1("SUB")

def cond():
    expr()
    if token in ["==","<>","<",">","<=",">="]:
        next_token()
        expr()
    
def affec():
    global token,PLACESYM
    #recherche de l'adresse de la variable
    ADDR=getAdresseFromTableSym(token)
    test_et_cherche(ID)
    generer2('LDA', ADDR)
    teste(":=")
    expr()
    generer1('STO')

def si():
    teste("if")
    cond()
    teste("then")
    generer2('BZE',0)
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
    generer1('PRN')
    while token==",":
        next_token()
        expr()
        generer1('PRN')
    teste(")")

def lire():
    teste("read")
    teste("(")
    nomVar=token
    test_et_cherche(ID)
    generer2('LDA',getAdresseFromTableSym(nomVar))
    generer1('INN')
    while token==",":
        next_token()
        nomVar=token
        teste(ID)
        generer2('LDA',getAdresseFromTableSym(nomVar))
        generer1('INN')
    teste(")")

def insts():
    teste("begin")
    inst()  
    while token==";":
        next_token()
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
    global offset
    if token=="const":
        consts()
    if token=="var":
        Vars()
    generer2('INT', offset)
    insts()
    
def program():
    teste("program")
    test_et_entre(ID, 'program')
    teste(";")
    block()
    generer1('HLT')
    if token != ".":
        erreur(".",token)
    
PCODE=[0]*50
PC=0
        
def generer1(m):
    global PCODE,PC
    if PC==len(PROGRAM):
        print('Error len')
    PCODE[PC]=m
    PC+=1
    
def generer2(m,a):
    global PCODE,PC
    if PC==len(PROGRAM):
        print('Error len')
    PCODE[PC]=(m,a)
    PC+=1
    
    
program()

print(PCODE)