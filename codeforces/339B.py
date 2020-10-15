n, m = list(map(int,input().split()))
li = list(map(int,input().split()))
count=0
dis = 0
i=1
li2 = []
while count<m:
    if i == li[count]:
        count+=1
    else:
        if li[count]>i:
            dif = li[count]-i
            dis+=dif
            i+=dif
        else:
            dif = n-i+li[count]
            dis+=dif
            i=li[count]

print(dis)



#         else:
#             break
#     if count==m:
#         break
#     else:
#         dis += 1
#         i+=1
#     if i>n:
#         i=1
#
# print(dis)
