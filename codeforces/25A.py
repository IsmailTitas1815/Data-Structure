n = int(input())
li = list(map(int,input().split()))[:n]
countOdd = 0
coundeven = 0
for i in li:
    if i%2==0:
        coundeven+=1
    else:
        countOdd+=1

if coundeven>countOdd:
    for i in range(n):
        if li[i]%2!=0:
            print(i+1)
            break
else:
    for i in range(n):
        if li[i]%2==0:
            print(i+1)
            break
