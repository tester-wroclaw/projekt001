#!/usr/bin/python
def f1(x, y=0):
    wynik = x*x+y
    return wynik

def f2(x):
    if len(x)==0:  
        return 'BUUUUM'
    else:        
        return x[0]

def f3(x):        
    return {
        1: "jeden",
        2: "dwa",
        3: "trzy",
        }.get(x,'other')

def f4(x, y=''):
    mk=' ma kota'
    i = ''
    if y!='':
        i = ' i ' + y
    return x + mk + i 
    
    