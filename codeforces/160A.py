n = int(input())
li = list(map(int,input().split()))[:n]
li.sort()
mypart = 0
count=0
sumoflist = sum(li)
for i in range(len(li)-1,-1,-1):
    if sumoflist-mypart >= mypart:
        mypart += li[i]
        count+=1
print(count)