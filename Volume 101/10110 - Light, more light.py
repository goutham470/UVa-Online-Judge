# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 21:08:18 2019

@author: gouth
"""
"""
import sys
sys.getrecursionlimit()
def lightswitch(n):
    def factorsof(n,i):
        if i<=n :
            if n%i==0:
                pflst.append(i)
                factors.append(int(n/i))
                if i==1: i+=1
                factorsof(n/i,i)
            else:
                factorsof(n,i+1)
    
    factorsof(n,1)
    if len(factors)%2==0:
        return "No"
    else:
        return "Yes"
    """


import sys

def lightswitch(n):
    pflst=[]
    factors=[]
    i=1
    while i<=n:
        if n%i==0:
            pflst.append(i)
            factors.append(int(n/i))
            n, i=n/i, i
            if i==1: i+=1
        else:
            n,i=n,i+1
    #return factors, pflst    
    if len(factors)%2==0:
        return "No"
    else:
        return "Yes"

if __name__ == "__main__":
    input=[]
    for line in sys.stdin:
        if int(line)==0 : break
        input.append(int(line))
    [print(lightswitch(int(n))) for n in input]
