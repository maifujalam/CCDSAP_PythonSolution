t=int(input())
for _ in range(t):
    n=int(input())
    a=input()
    l=a[:len(a)//2]
    if len(a)%2!=0:
        r=a[(len(a)//2)+1:]
    else:
        r=a[(len(a)//2):]
    flag=0
    for i in l:
        if l.count(i)!=r.count(i):
            flag=1
            break
    if flag==0:
        print("YES")
    else:
        print("NO")

