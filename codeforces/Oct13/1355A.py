for i in range(int(input())):
    a,n = list(map(int,input().split()))
    for j in range(2,n+1):
        a = str(a)
        li = [int(k) for k in a]
        if 0 in li:
            break
        else:
            li.sort()
            a = int(int(a) + (min(li) * max(li)))
    print(a)
