import time
'''def sub(s):
    a=[s]
    if len(s)>0:
        a.extend(sub(s[1:]))
        a.extend(sub(s[:-1]))
    else:
        return []
    return a
    
st="11111"
st1=sub(st)
fn=[st]
for i in st1:
    if i not in fn:
        fn.append(i)
print(fn)'''

'''
def sub(s):
    l=[]
    for i in range(len(s)+1):
        for j in range(i):
            pp=s[j:i]
            l.append(pp)
            #print(j,i,s[j:i])
    return l

t=int(input())
while t>0:
    t-=1
    l=int(input())
    s=input()
    su=sub(s)
    ct=0
    for i in su:
        if i[0]=='1' and i[-1]=='1':
            ct+=1
    print(su,ct)
'''
t=int(input())
for _ in range(t):
    n=int(input())
    a=input()
    c=a.count("1")
    su=0
    for i in range(c):
        su=su+c-i
    print(su)
