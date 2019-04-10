# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 00:00:34 2019
@author: gouth

Done
"""   
colorlst=['BCG','BGC','CBG','GBC','CGB','GCB']
codelst=['021','012','120','102','210','201']
mydict={}
for i in range(0,len(colorlst)):
    mydict[colorlst[i]]=codelst[i]

def minmovments(b,g,c):
    maxtup=()
    maxval=4294967295
    for k,v in mydict.items():
        #print("key:",k,"Value:",v)
        x,y,z=b.copy(),g.copy(),c.copy()
        del x[int(v[0])]
        del y[int(v[1])]
        del z[int(v[2])]
        value=sum(x+y+z)
        if value<maxval:
            maxtup=(k,value)
            maxval=value
            #print("key:",k,"Value:",value)
    return  maxtup

import sys
if __name__=="__main__":
    lst=[]
    for line in sys.stdin:
        ln=line.split()
        if len(ln)!=9:
            break
        lst.append(list(map(int,ln)))
    for i in lst:
        b=[i[0],i[3],i[6]]
        g=[i[1],i[4],i[7]]
        c=[i[2],i[5],i[8]]
        res=minmovments(b,g,c)
        print("{} {}".format(res[0],res[1]))