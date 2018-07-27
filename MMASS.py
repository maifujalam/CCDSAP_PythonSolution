a=input().strip()
a=list(a)
dic={'H':1,'C':12,'O':16}
dic0=['H','C','O']
dig=['1','2','3','4','5','6','7','8','9']
op=[]
tm=[]
b=[]
for i in range(len(a)):
    if a[i] in dig and a[i-1] in dic0:
        pp=(int(a[i])-1)
        for ii in range(pp):
            b.append(a[i-1])
    else:
        b.append(a[i])
#print(b)
for i in b:
    if i in dic or i in '(':
        op.append(i)
    elif i==')':
        tm=[]
        while op!=[] and op[-1]!='(':
            tm.append(op.pop())
        if op[-1]=='(':
            op.pop()
        op.extend(tm)
    elif i in dig:
        val=int(i)-1
        op.extend(val*tm)
        tm=[]
    #print(op)
h1=op.count('H')
c1=op.count('C')
o1=op.count('O')
#print(op,h1,c1,o1)
print(h1+c1*12+o1*16)
