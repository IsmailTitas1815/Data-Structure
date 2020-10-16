count=0
for i in range(int(input())):
    li = list(map(int,input().split()))[:3]
    if sum(li)>1:
        count+=1
print(count)