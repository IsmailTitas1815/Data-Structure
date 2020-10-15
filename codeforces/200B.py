n = int(input())
li = list(map(float,input().split()))[:n]
s = sum(li)
print(format(s/n,'.12f'))
