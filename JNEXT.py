t=int(input())


def per(a):
    l=len(a)
    i=l-2
    while i>=0 and a[i]>=a[i+1]:
        i-=1
    if i==-1:
        print(-1)
    j=i+1
    while j<l and a[j]>a[i]:
        j+=1
    j-=1
    a[i],a[j]=a[j],a[i]
    a[i+1:]=a[len(a)-1:i:-1]
    print("".join(map(str,a)))


while t>0:
    t-=1
    n=int(input())
    a=[int(i) for i in input().split()]
    per(a)
