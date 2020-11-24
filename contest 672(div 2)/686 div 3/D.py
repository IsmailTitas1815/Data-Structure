def primeSieve(li):
    for i in range(3,100000000000000,2):
        li[i]= 1

    for i in range(3,100000000000000,2):
        if li[i]==1:
            for j in range(i*i,100000000000000,i):
                li[j]=0

    li[2]=1


li = [0]*100000000000005
primeSieve(li)
n = int(input())
if n in li:
    flag = True
else:
    flag = False

if flag:
    print(n)
else:
    pass

