# testcase = int(input())
#
# for i in range(testcase):
#     k = 10
#     count=0
#     li=[1,2,3,4,5,6,7,8,9,10]
#     a,b = list(map(int,input().split()))
#     if a==b:
#         print(count)
#     else:
#         if a<b:
#             for j in range(k,0,-1):
#                 while (a+j)<=b:
#                     a = a+j
#                     count+=1
#                     if a==b:
#                         break
#
#
#         else:
#             for j in range(k,0,-1):
#                 while (a-j)>=b:
#                     a = a-j
#                     count+=1
#                     if a==b:
#                         break
#
#         print(count)






#----------------------------------------------------------------





testcase = int(input())

for i in range(testcase):
    a,b = list(map(int,input().split()))
    k = 10
    count=0
    if a==b:
        print(count)
    else:
        if a<b:
            while k>=1:
                if (a+k)<=b:
                    a = a+k
                    count+=1
                    if a==b:
                        break
                else:
                    k-=1


        else:
            while k>=1:
                if (a - k) >= b:
                    a = a - k
                    count += 1
                    if a == b:
                        break
                else:
                    k -= 1

        print(count)