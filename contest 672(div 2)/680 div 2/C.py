#
import math
#
# def divisorGenerator(n):
#     large_divisors = []
#     for i in range(1, int(math.sqrt(n) + 1)):
#         if n % i == 0:
#             yield i
#             if i*i != n:
#                 large_divisors.append(n / i)
#     for divisor in reversed(large_divisors):
#         yield divisor
#
# for i in range(int(input())):
#     p,q = list(map(int,input().split()))
#     li = list(map(int,list(divisorGenerator(p))))
#     li.reverse()
#     for j in range(len(li)):
#         if li[j]%q!=0:
#             print(li[j])
#             break
#

def FindAllDivisors(x,q):
    divList = []
    y = 1
    while y <= math.sqrt(x):
        if x % y == 0:
            divList.append(y)
            if(int(x/y)%q!=0):
                divList.append(int(x / y))
        y += 1
    return divList
for i in range(int(input())):
    p,q = list(map(int,input().split()))
    if p%q!=0:
        print(p)
    else:
        li = FindAllDivisors(p,q)
        m = max(li)
        print(m)
