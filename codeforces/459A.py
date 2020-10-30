li = list(map(int,input().split()))[:4]
if len(set(li))>2:
    print(-1)
else:
    for i in range(1,len(li)):
        if li[i-1] == 0 and li[i] == 0:
            li[i] = 1



    print(*li,sep=" ")