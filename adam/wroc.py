#!/usr/bin/python
def f1(x, y=0):
    wynik = x*x+y
    return wynik

def f2(x):
    if len(x)==0:  
        return 'BUUUUM'
    else:        
        return x[0]
   