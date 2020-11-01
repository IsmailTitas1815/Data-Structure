# def sievePrime(li,n):
#     li[2]=1
#     for i in range(3,n,2):
#         li[i] = 1
#     k = 2
#     while k*k<=n:
#         if li[k]==1:
#             for j in range(k*k,n,k):
#                 li[j]=0
#         k+=1
# for i in range(int(input())):
#     m,n = list(map(int,input().split()))
#     li = [0]*(n+1)
#     sievePrime(li,n)


def primeSieve(li):
    for i in range(3,1000000,2):
        li[i]= 1

    for i in range(3,1000000,2):
        if li[i]==1:
            for j in range(i*i,1000000,i):
                li[j]=0

    li[2]=1

li = [0]*10000005
primeSieve(li)

count = [0]*10000005
for i in range(1,1000000):
    count[i] = count[i-1] + li[i]

for i in range(int(input())):
    a,b = list(map(int,input().split()))
    print(count[b]- count[a-1])