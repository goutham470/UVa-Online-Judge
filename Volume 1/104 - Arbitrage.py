def arbitage(plen):
    lst1=list(permutations(lst,plen))
    for j in [[0]+list(i)+[0] for i in lst1]:
        val=1
        length=len(j)
        print([x+1 for x in j])
        index=0
        for k in j:
            if index+1>=length:
                break
            print("index:{}, index+1:{},val:{}".format(j[index],j[index+1],vals[j[index]][j[index+1]]))
            val=vals[j[index]][j[index+1]]*val
            index+=1
        print(val,(val-1)*100)

arbitage(1)
if __name__=="__main__":
    dim=int(input())
    lst=list(range(0,dim))
    vals=[]
    counter=0
    for line in sys.stdin:
        temp = list(map(float, line.split()))
        temp.insert(counter,1)
        counter+=1
        vals.append(temp)
    print(vals)