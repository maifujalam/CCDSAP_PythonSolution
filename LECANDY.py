t=int(input())
while t>0:
    t=t-1
    n,c=map(int,input().split())
    a=[int(i) for i in input().split()]
    re=sum(a)
    if re>c:
        print("No")
    else:
        print("Yes")
