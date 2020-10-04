n = int(input())
for i in range(n):
    li = list(map(int,input().split()))[:3]
    print(min(li)+max(li))