t = int(input())
for i in range(t):
    n = int(input())
    m = 0
    total = 0
    while True:
        m+=1
        total+=m
        if total == n:
            print(m)
            break
        elif total-1==n:
            print(m+1)
            break
        elif total>n+1:
            print(m)
            break