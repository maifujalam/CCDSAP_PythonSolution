t=int(input())
while t>0:
    t-=1
    n=int(input())
    a=[int(i) for i in input().split()]
    c=[]
    flag=0
    for i in range(len(a)//2):
        if a[i]==a[len(a)-i-1]:
            c.append(a[i])
        else:
            flag=1
            break
    if len(a)%2!=0:
        c.append(a[len(a)//2])
    c=set(c)
    #print(c,flag)
    if sum(c)==28 and flag==0:
        print("yes")
    else:
        print("no")

