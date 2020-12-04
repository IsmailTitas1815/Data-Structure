t = int(input())
for i in range(t):
    n,m = list(map(int,input().split()))
    lin = list(map(int,input().split()))[:n]
    lim = list(map(int,input().split()))[:m]
    final = list(set(lin)&set(lim))
    print(len(final))