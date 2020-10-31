import collections
n = int(input())
li = list(map(int,input().split()))[:n]
l = len(li)
li2 = sorted(li)
count = 0

for i in range(l):
    if li == li2:
        break
    else:
        li = collections.deque(li)
        li.rotate(1)
        li = list(li)
        count+=1

if count==l:
    print(-1)
else:
    print(count)