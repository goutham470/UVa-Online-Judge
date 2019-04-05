# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 08:23:12 2019

@author: gouth
"""

lst=[]
def blockInit(n):
    if len(lst)==0:
        for i in range(0,n):
            lst.append([i])
        return lst

def blockShuffle(op,a,b):
    print(lst)
    if op=="00":  #move a onto b = reorg a,b on top of b 
        reorgBlocks(lst[a])
        reorgBlocks(lst[b])
        lst[b]=[b]+[a]
        lst[a]=[]
    elif op=="01":  #move a over b = reorg a on top of b stack
        reorgBlocks(lst[a])
        lst[b]=lst[b]+[a]
        lst[a]=[]                
    elif op=="10":  #pile a onto b = reorg b and place a stack on top of b
        reorgBlocks(lst[b])
        lst[b]=[b]+lst[a]
        lst[a]=[]
    else:  #pile a over b = pile a stack on top of b stack
        lst[b]=lst[b]+lst[a]
        lst[a]=[]
        
def reorgBlocks(x):
    if x is not None:
        for i in x:
            lst[i]=[i]

import sys
if __name__=="__main__":
    n=int(input())
    print(blockInit(n))
    
    for line in sys.stdin:
        ln=line.split()
        if ln[0]=="quit":
            for i in lst:
                index=0
                print("{}: {}".format(index," ".join([str(j) for j in i])))
                index+=1
            break
        if ln[0] not in ("move","pile") or ln[2] not in ("onto","over"): continue
        a,b=int(ln[1]),int(ln[3])
        op=("1" if ln[0]=="move" else "0")+("1" if ln[0]=="move" else "0")
        blockShuffle(op,a,b)
        
            
        
        

            