while True:
    n=int(input())
    if n==0:
        break
    flag=0
    a=[int(i) for i in input().split()]
    k=1
    t=[]
    x=[]
    ll=len(a)
    a.reverse()
    while len(a)!=0:
        pp=a.pop()
        if pp==k:
            x.append(pp)
            k+=1
        elif pp!=k:
            t.append(pp)
        while t!=[] and x!=[]:
            tm=t[len(t)-1]
            #print(x[len(x)-1],tm)
            if x[len(x)-1]+1==tm:
                x.append(tm)
                t.pop()
            else:
                break
    if len(x)==n:
        print("yes")
    else:
        print("no")

