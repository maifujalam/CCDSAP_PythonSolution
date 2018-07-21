t=int(input())
while t>0:
    t=t-1
    x,y,k,n=map(int,input().split())
    req=x-y
    flag=0
    while n>0:
        n=n-1
        p,c=map(int,input().split())
        if c<=k and req<=p:
            flag=1
    if flag==1:
        print("LuckyChef")
    else:
        print("UnluckyChef")


