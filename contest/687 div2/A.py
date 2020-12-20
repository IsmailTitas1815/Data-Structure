for i in range(int(input())):
    n,m,r,c = list(map(int,input().split()))
    if r<=n//2:
        first = n
    else:
        first = 1
    if c<=m//2:
        second = m
    else:
        second = 1

    print(abs(first-r)+abs(second-c))