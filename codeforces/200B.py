n = int(input())
li = list(map(float,input().split()))[:n]
s = sum(li)
print(round(s/n,12))
