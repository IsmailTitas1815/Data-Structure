n,m = list(map(int,input().split()))
li = list(map(int,input().split()))[:n]
count=0
for i in range(1,len(li)):
    if (li[i]-li[i-1]) <= m:
        count+=1
    else:
        count = 0

print(count+1)
