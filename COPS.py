t=int(input())
while t>0:
    t-=1
    M,x,y=map(int,input().split())
    a=[int(i) for i in input().split()]
    h=[0 for i in range(100)]
    cst=x*y
    for i in a:
        i=i-1
        r=i
        ll=i-1
        for j in range(cst+1):
            if r<len(h):
                h[r]=1
                r=r+1
        for k in range(cst):
            if ll>=0:
                h[ll]=1
                ll=ll-1
    ct=0
    for i in range(100):
        if h[i]==0:
            ct+=1
    print(ct)
