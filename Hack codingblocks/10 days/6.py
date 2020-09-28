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


def primes_sieve1(limit):
    limitn = limit+1
    primes = dict()
    for i in range(2, limitn):
        primes[i] = True
    for i in primes:
        factors = range(i,limitn, i)
        for f in factors[1:]:
            primes[f] = False
    return [i for i in primes if primes[i]==True]

print (primes_sieve1(200))