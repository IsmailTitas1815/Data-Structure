for i in range(int(input())):
    n = int(input())
    li = list(map(int,input().split()))[:n]
    if n%2==0:
        mid = n//2
        for j in range(mid):
            print(li[j], li[n - 1 - j], end=" ")
        print()
    else:
        mid = n//2 +1
        for j in range(mid-1):
            print(li[j], li[n - 1 - j], end=" ")
        print(li[mid-1])


