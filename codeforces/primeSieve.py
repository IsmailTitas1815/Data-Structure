def primeSieve(li):
    for i in range(3,1000000,2):
        li[i]= 1

    for i in range(3,1000000,2):
        for j in range(i*i,1000000,i):
            li[j]=0

    li[2]=1


li = [0]*10000005
primeSieve(li)
primelist = []
count = 0
n = int(input())
for i in range(n+1):
    if li[i]==1:
        primelist.append(i)
        count+=1
print(primelist)
print(count)
