def per(a):
    l=len(a)
    i=l-2
    while i>=0 and a[i]>=a[i+1]:
        i-=1
    if i==-1:
        return False
    j=i+1
    while j<l and a[j]>a[i]:
        j+=1
    j-=1
    a[i],a[j]=a[j],a[i]
    a[i+1:]=a[len(a)-1:i:-1]
    return True

a=[1,4,7,4,5,8,4,1,2,6]
print(a)
while True:
    if per(a):
        print(a)


