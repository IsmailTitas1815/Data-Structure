# import math
# n = int(input())
# li = list(map(int,input().split()))[:n]
#
# for i in li:
#     if i>3:
#         c = 0
#         div = math.ceil(math.sqrt(i))
#         if div <7:
#             for j in range(2,math.ceil(i/2)+1):
#                 if i % j == 0:
#                     c += 1
#             if c == 1:
#                 print("YES")
#             else:
#                 print("NO")
#         else:
#             for j in range(2,div+1):
#                 if i%j==0:
#                     c+=1
#             if c==1:
#                 print("YES")
#             else:
#                 print("NO")
#     else:
#         print("NO")

# def perfectsqrt(n):
#     if sqrt(n)*sqrt(n) == n:
#         return 1
#     else:
#         return 0
#
# from math import sqrt,ceil
# n = int(input())
# li = list(map(int,input().split()))[:n]
#
# for i in li:
#     c=0
#     if i < 4:
#         print("NO")
#     elif i==4:
#         print("YES")
#     else:
#         if i%2==0:
#             print("NO")
#         else:
#             if i % sqrt(i) == 0:
#                 c+=1
#                 i = i / sqrt(i)
#             div = ceil(sqrt(i))
#             for j in range(3,div+1):
#                 if i%j == 0:
#                     c+=1
#             if c==1:
#                 print("YES")
#             else:
#                 print("NO")


# import math
# def printDivisors(n):
#     # Note that this loop runs till square root
#     i = 1
#     while i <= math.sqrt(n):
#
#         if (n % i == 0):
#             # If divisors are equal, print only one
#             if (n / i == i):
#                 print(i)
#             else:
#                 # Otherwise print both
#                 print(i, n / i)
#         i = i + 1
#
# print("The divisors of 100 are: ")
# printDivisors(int(997))

# 999966000289



















#
#
#
#
#
#
#
def perfectsqrt(n):
    if n % sqrt(n) == 0:
        return 1
    else:
        return 0

from math import sqrt,ceil
n = int(input())
li = list(map(int,input().split()))[:n]

for i in li:
    c=0
    if i < 4:
        print("NO")
    elif i==4:
        print("YES")
    else:
        if i%2==0:
            print("NO")
        else:
            if i>49:
                if i%3!=0 and i%5!=0 and i%7!=0 and perfectsqrt(i)==1:
                    if sqrt(i)%3!=0 and sqrt(i)%5!=0 and sqrt(i)%7!=0:
                        print("YES")
                    else:
                        print("NO")
                else:
                    print("NO")
            else:
                if perfectsqrt(i)==1:
                    print("YES")
                else:
                    print("NO")

# 1000000000000 999999999999 999999999998 999999999997 999999999996 999999999995 999999999994 999999999993 999999999992 999999999991 999999999990 1000000000089 999999999988 999999999987 999999999986 999999999985 999999999984 999999999983 999999999982 999999999981 999999999980