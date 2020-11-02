li = []
n = int(input())
for i in range(n):
    li2 = list(map(int,input().split()))[:n]
    li.append(li2)
nextLi = []
for i in range(n-1,-1,-1):
    mini = []
    for j in range(n):
        mini.append(li[j][i])
    nextLi.append(mini)

for i in range(n):
    print(*nextLi[i],sep=" ")
