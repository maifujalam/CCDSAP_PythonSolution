import string



alp=string.ascii_letters
precedences={'^':3,'/':2,'*':2,'-':1,'+':1}


def weight(i,st):
    try:
        a1=precedences[i]
        a2=precedences[st[-1]]
        return True if a1<=a2 else  False
    except KeyError:
        return False

def PreToPostfix(a):
    op=[]
    st=[]
    for i in a:
        if i in alp:
            op.append(i)
        elif i=='(':
            st.append(i)
        elif i==')':
            while st!=[] and st[-1]!='(':
                op.append(st.pop())
            st.pop()
        else:
            while st!=[] and weight(i,st):
                op.append(st.pop())
            st.append(i)
    while st!=[]:
        op.append(st.pop)
    print("".join(op))

t=int(input())
while t>0:
    t-=1
    a=input()
    a=list(a)
    PreToPostfix(a)
