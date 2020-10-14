# for i in range(int(input())):
#     n,x = list(map(int,input().split()))
#     li = list(map(int,input().split()))
#     liEven = [i for i in li if i%2==0]
#     liOdd = [i for i in li if i%2==1]
#     sum = 0
#     if n==1:
#         if li[0]%2==0:
#             print("NO")
#         else:
#             print("YES")
#     else:
#         if len(liOdd)>0:
#             sum += liOdd[0]
#         i = 0
#         # print("first",sum)
#         while i+1<x and i+1<len(liOdd):
#             sum = liOdd[i+1]
#             i+=1
#         # print(sum)
#         if i==x-1:
#             if sum%2==0:
#                 print("NO")
#             else:
#                 print("YES")
#             # print("odd",sum)
#
#         else:
#             baki = x-i-1
#             for j in range(baki+1):
#                 sum = liEven[j]
#             if sum%2==0:
#                 print("NO")
#             else:
#                 print("YES")
#             # print("even",sum)

for i in range(int(input())):
    n,x = list(map(int,input().split()))
    li = list(map(int,input().split()))[:n]
    sum = 0
    odd = 0
    even = 0
    for j in range(len(li)):
        if li[j]%2==0:
            even+=1
        else:
            odd+=1
    if odd == 0:
        print("NO")
    else:
        odd-=1
        x-=1
        while x>0:
            if odd>=2 and x>=2:
                odd-=2
                x-=2
            elif even>0:
                even-=1
                x-=1
            else:
                break
        if x==0:
            print("YES")
        else:
            print("NO")
