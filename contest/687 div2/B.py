from collections import Counter
from  math import ceil
t = int(input())
for i in range(t):
    n, k = list(map(int,input().split()))
    li = list(map(int,input().split()))[:n]
    c = dict(Counter(li))
    # print(c)
    m = max(c.values())
    # print(m)
    baki = n - m
    # print(baki)
    days = ceil(baki/k)
    print(days)
