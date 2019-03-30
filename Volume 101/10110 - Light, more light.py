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


primeslst=[2,3,5,7]

def nextoddnum(n):
    if n%2==0 or n%3==0 or n%5==0 or n%7==0 :
        n=nextoddnum(n+1)
    return n


def isprime(i):
    flag=True
    for x in [k for k in primeslst if i%k==0 and k<=math.sqrt(i)]:
        if i%x==0:
            flag=False
            break
    return flag

#nextoddnum(11+1)
#isprime(19)
#primefactors(76)
#lightswitch(76)


def primefactors(n):##Returns primes less than square root
    i=11
    while i<=math.sqrt(n):
        if isprime(i):
            primeslst.append(i)
            i=nextoddnum(i+1)
        else:
            i=nextoddnum(i+1)
    return primeslst



#print(primefactors(1426539184))


def lightswitch(n):
    if n==1: return "Yes"
    elif n==2 : return "No"
    
    pflst=[i for i in primeslst if n%i==0]
    factors={1,n}
    for i in pflst:
        counter=1
        while i<=n: 
            if n%i==0:
                factors.add(int(n/i))
                factors.add(math.pow(i,counter))
                counter+=1
                n, i=n/i, i
            else:
                break
    #return factors, pflst  
    #print(factors,pflst)
    if len(factors)%2==0:
        return "No"
    else:
        return "Yes"


if __name__ == "__main__":
    input=[]
    for line in sys.stdin:
        if int(line)==0 : break
        input.append(int(line))
    primeslst=primefactors(max(input))
    [print(n,lightswitch(int(n))) for n in input]

#%time primefactors(1000)
#%time lightswitch(3)