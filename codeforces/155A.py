t = int(input())
li = list(map(int,input().split()))[:t]
min = li[0]
max = li[0]
count = 0
for i in range(1,t):
    if li[i]<min:
        min = li[i]
        count+=1
    elif li[i]>max:
        max = li[i]
        count+=1
print(count)


