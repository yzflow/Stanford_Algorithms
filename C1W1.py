# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def multi(x, y):
    x=str(x)
    y=str(y)
    n = int(len(x))
    if n == 1:
        x=int(x)
        y=int(y)
        return x*y
    m = int(n/2)
    a = x[:m]
    b = x[m:]
    c = y[:m]
    d = y[m:]
    if len(a) == 1 and len(b) == 1 and len(c) == 1 and len(d) ==1:
        a = int(a)
        b = int(b)
        c = int(c)
        d = int(d)
        return 10**2*a*c+10*(a*d+b*c)+b*d
    else:
        a = int(a)
        b = int(b)
        c = int(c)
        d = int(d)
        return int(10**(n)*multi(a, c)+10**(n/2)*(multi(a,d)+multi(b,c))+multi(b,d))
