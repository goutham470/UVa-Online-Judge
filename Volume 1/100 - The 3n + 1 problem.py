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


def main(argv):
    i=int(argv[0])
    j=int(argv[1])
    global mydict
    for n in range(i,j+1):
        seqgen(n)
        
    print(i,j,max(list(mydict.values())))

if __name__ == "__main__":
    main(sys.argv[1:])