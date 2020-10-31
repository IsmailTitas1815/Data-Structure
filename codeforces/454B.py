# import collections
# n = int(input())
# li = list(map(int,input().split()))[:n]
# l = len(li)
# li2 = sorted(li)
# count = 0
#
# for i in range(l):
#     if li == li2:
#         break
#     else:
#         li = collections.deque(li)
#         li.rotate(1)
#         li = list(li)
#         count+=1
#
# if count==l:
#     print(-1)
# else:
#     print(count)


n = int(input())
li = list(map(int,input().split()))[:n]
li2 = sorted(li)
count=0
pos = 0
for i in range(n):
    if li[i-1]>li[i]:
        count+=1
        pos = i
if li==li2:
    print(0)
elif count>1:
    print(-1)
else:
    print(n-pos)
