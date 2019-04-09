#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 21:51:02 2019

@author: gouth
Correct but Giving Error
"""
import sys

mydict={1:1}
def seqgen(n):
    if n in mydict.keys():
        return mydict[n]
    
    if n==1:
        return 1
    
    if n%2!=0: 
        k=1+seqgen(3*n+1)
        mydict[n]=k
        return k
    else:
        k=1+seqgen(n/2)
        mydict[n]=k
        return k


def max_cycle(bounds):
    i,j = bounds
    global mydict
    mydict={}
    for n in range(i,j+1):
        seqgen(n)
    
    return max(list(mydict.values()))

if __name__ == "__main__":
    input=[]
    for line in sys.stdin:
        ln=line.split()
        if len(ln)!=2:
            break
        bounds = tuple(sorted(map(int, ln)))
        input.append(bounds)
    
    [print("{} {} {}".format(x[0], x[1], max_cycle(x))) for x in input]
