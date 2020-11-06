for i in range(int(input())):
    n = int(input())
    li = list(map(int,input().split()))[:n]
    mid = n//2
    li.reverse()
    print(*li,sep=' ')
    # if n%2==0:
    #     print(*li,sep=' ')
    # else:
    #     li[mid] ,li[mid-1] = li[mid-1],li[mid]
    #     print(*li,sep=" ")
