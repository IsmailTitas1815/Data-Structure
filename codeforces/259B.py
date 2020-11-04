li = []
for i in range(3):
    minLi = list(map(int,input().split()))[:3]
    li.append(minLi)

s = 0

for i in range(3):
    s+=sum(li[i])
half = s//2

for i in range(3):
    indx = li[i].index(0)
    li[i][indx] = half - sum(li[i])

for i in range(3):
    print(*li[i],sep=" ")
