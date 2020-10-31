li = list(map(int,input().split()))
li.sort()
s = 0
for i in range(li[0],li[0]+1):
    for j in range(li[0],li[1]+1):
        for k in range(li[0],li[2]+1):
            s += (i*j*k)


print(s)

