# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 22:32:47 2019

@author: gouth
"""
import sys
#lst=[(1,2),(3,5),(3,1),(2,4),(4,5)]
def LongestPath(s,lst):
    x=s
    counter=0
    
     
    while len(x)!=0:
        last=x[0]
        x=[(i[1]) for i in lst if i[0] in x]
        counter+=1
    return (counter-1,last)
        
#LongestPath(3)        
if __name__=="__main__":
    lst=[]
    case=[]
    start=[]
    while True:
        n=int(input())
        if n == 0:
            break
        case.append(n)
        start.append(int(input()))##2nd argument
        temp=[]
        for line in sys.stdin:
            ln=line.split()
            if int(ln[0])==0 and int(ln[1])==0:
                break
            bounds = tuple(map(int, ln))
            temp.append(bounds)
        lst.append(temp)
    for i in range(0,len(case)):
        res=LongestPath(start[i],lst[i])
        print("Case {}: The longest path from {} has length {}, finishing at {}.".format(i+1,start[i],res[0],res[1]))

