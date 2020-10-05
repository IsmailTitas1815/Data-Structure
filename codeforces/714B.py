# n = int(input())
# li = list(map(int,input().split()))[:n]
# if n<=2:
#     print("YES")
#
# else:
#     li.sort()
#     half = len(li) // 2
#     mid = li[half]
#     flag1 = 0
#     flag2 = 0
#     choto = mid
#     for i in range(half, -1, -1):
#         if mid > li[i]:
#             choto = li[i]
#             break
#     diff = mid - choto
    # mid er boro ta ber korte hobe
    # for i in range(half, -1, -1):
    #     if mid > li[i]:
    #         choto = li[i]
    #         break
    # diff = mid - choto
    # for i in range(half,-1,-1):
    #     if mid - li[i] == 0 or mid - li[i]== diff:
    #         flag1 = 1
    #     else:
    #         flag1 = 0
    #         break
    # for j in range(half+1,len(li),1):
    #     if li[j]-mid == 0 or li[j] - mid == diff:
    #         flag2 = 1
    #     else:
    #         flag2 = 0
    #         break
    # if flag1==1 and flag2 ==1:
    #     print("YES")
    # elif flag1==0 or flag2 ==0:
    #     print("NO")

# 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000
# 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000
# 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000
# 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000
# 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000
# 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000
# 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000
# 1000000000 1000000000 1000000000




n = int(input())
s = set(map(int,input().split()))

if len(s)>3:
    print("NO")
elif len(s) == 1 or len(s) == 2:
    print("YES")
else:
    li = sorted(list(s))
    if li[1]-li[0] == li[2] - li[1]:
        print("YES")
    else:
        print("NO")
