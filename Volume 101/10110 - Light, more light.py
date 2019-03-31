# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 21:08:18 2019

@author: goutham
10-> 1,2,  |sqrt(10)|  5,10
8->  1,2,  |sqrt(8) |  4,8
16-> 1,2,  |4       |  ,8,16
Initial State is OFF.
All no.s have equal no. factors on either side of square root(so which form a pair of OFF->ON->OFF ) a no. having a perfect square root will have one more integer  as its factor making it ON.
so if it has a perfect sq root -> ON
else -> OFF
"""
import sys
import math

def lightswitch(n):
    x=math.sqrt(n)
    if x-int(x)>0:
        return "no"
    else:
        return "yes"

if __name__ == "__main__":
    input=[]
    for line in sys.stdin:
        if int(line)==0 : break
        input.append(int(line))
    [print(lightswitch(int(n))) for n in input]

#%time lightswitch(3)
