# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 23:28:53 2019

@author: gouth
"""

def carries(a,b):
    carry=0
    count=0
    while a!=0 or b!=0:
        if a%10+b%10+carry >=10:
            count+=1
            carry=1
        elif a%10+b%10+carry <10:
            carry=0
        print(a,b)    
        a,b=int(a/10),int(b/10)
    if count==0:
        return "No"
    else:
        return count
        
if __name__=="__main__":
    print(carries(123,594)," carry operations")
        
        
        
            