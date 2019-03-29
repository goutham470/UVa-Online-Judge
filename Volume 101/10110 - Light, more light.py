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
import math


def primefactors(n):
    primes=[2]
    i=2
    while i<=math.sqrt(n):
        if min([i%x for x in primes ])==0:
            i=nextoddnum(i+1)
        else:
            primes.append(i)
            i=i+1
    return primes


def nextoddnum(n):
    if n%2==0 :
        n=nextoddnum(n+1)
    return n


def lightswitch(n):
    if n<=2: return "No"
    pflst=primefactors(n)
    factors=[]
    for j in pflst:
        i=j
        while j<n: 
            if n%i==0:
                pflst.append(i)
                factors.append(int(n/i))
                n, i=n/i, i
            else:
                break
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

#%time primefactors(1000)
#%time lightswitch(3)