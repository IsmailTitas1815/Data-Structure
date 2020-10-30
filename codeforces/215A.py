n = int(input())
li = list(map(int,input().split()))[:n]
m = int(input())
li2 = list(map(int,input().split()))[:m]
count = 0
l = []
for i in range(len(li2)):
    for j in range(len(li)):
        if li2[i]%li[j]==0:
            l.append(li2[i]/li[j])

m = max(l)
count=0
for i in li:
    if (i*m) in li2:
        count+=1

print(count)