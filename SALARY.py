import sys,time
t=int(input())
while t>0:
    t=t-1
    n=int(sys.stdin.readline())
    sa=[int(i) for i in sys.stdin.readline().split()]
    ct=0
    while max(sa)!=min(sa):
        ma=max(sa)
        lo=sa.index(ma)
        j=0
        for i in range(len(sa)):
            if i != lo:
                sa[i]=sa[i]+1
        ct+=1
        print(sa)
    sys.stdout.write(str(ct))







