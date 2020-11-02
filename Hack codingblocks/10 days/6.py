# testcases = int(input())
# for i in range(testcases):
#     # a,b = list(map(int,input().split()))
#     # count=0
#     # for j in range(a,b+1):
#     #     flag = True
#     #     if j>1:
#     #         for k in range(2,j):
#     #             if j%k==0:
#     #                 flag = False
#     #                 break
#     #         if flag:
#     #             count+=1
#     lower,upper = list(map(int,input().split()))
#     count=0
#     for num in range(lower, upper + 1):
#         if num>1:
#             for i in range(2,num//2+1):
#                 if num%i==0:
#                     break
#             else:
#                 count+=1
#     print(count)

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