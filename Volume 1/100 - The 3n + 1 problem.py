#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 21:51:02 2019

@author: gouth
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
    for line in sys.stdin:
        ln=line.split()
        if len(ln)!=2:
            break
        bounds = tuple(sorted(map(int, ln)))
        max_cycle(bounds)
        print("{} {} {}".format(ln[0], ln[1], max(list(mydict.values()))))
