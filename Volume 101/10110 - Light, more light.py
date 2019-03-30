# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 21:08:18 2019

@author: gouth
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