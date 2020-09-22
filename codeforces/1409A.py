

from math import ceil
testcase = int(input())

for i in range(testcase):
    k = 10
    count=0
    n = 0
    a,b = list(map(int, input().split()))
    if a==b:
        print(count)
    else:
        if a>b:
            max = a
            min = b
            diff = a-b
        else:
            max = b
            min = a
            diff = b-a

        count = diff // 10
        if diff%10 != 0:
            count+=1
        print(count)

#----------------------------------Solved




# testcase = int(input())
#
# for i in range(testcase):
#     k = 10
#     count=0
#     # rem= 0
#     n = 0
#     a,b = list(map(int,input().split()))
#     if a==b:
#         print(count)
#     else:
#         if a>b:
#             max = a
#             min = b
#             diff = a-b
#         else:
#             max = b
#             min = a
#             diff = b-a
#         while True:
#             if diff>=k:
#                 if diff/k < k:
#                     count+= diff//k
#                     rem = diff%k
#                     if rem!=0:
#                         count+=1
#                         break
#                 else:
#                     olddiff = diff
#                     diff = diff//k
#                     rem = diff%10
#                     count += (olddiff-diff)//k
#                     if rem!=0:
#                         if n==0:
#                             count+=1
#                             n+=1
#
#             else:
#                 count+=1
#                 break
#         print(count)
#
#
#
#
#
# #----------------------------------------------------------------
#
#
#
#
#
# # testcase = int(input())
# #
# # for i in range(testcase):
# #     a,b = list(map(int,input().split()))
# #     k = 10
# #     count=0
# #     if a==b:
# #         print(count)
# #     else:
# #         if a<b:
# #             while k>=1:
# #                 if (a+k)<=b:
# #                     a = a+k
# #                     count+=1
# #                     if a==b:
# #                         break
# #                 else:
# #                     k-=1
# #
# #
# #         else:
# #             while k>=1:
# #                 if (a - k) >= b:
# #                     a = a - k
# #                     count += 1
# #                     if a == b:
# #                         break
# #                 else:
# #                     k -= 1
# #
# #         print(count)