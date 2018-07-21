for i in range(1,10000):
    flag=0
    for j in range(1,10):
        if(i%j!=0):
            flag=1
            break

    if flag==0:
        print(i)




