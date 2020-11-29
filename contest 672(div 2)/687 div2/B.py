from collections import Counter
from  math import ceil
t = int(input())
for i in range(t):
    n, k = list(map(int,input().split()))
    li = list(map(int,input().split()))[:n]
    count = dict(Counter(li))
    m = max(count.values())
    baki = n - m
    days = ceil(baki/k)
    print(days)

