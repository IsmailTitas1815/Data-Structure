for i in range(int(input())):
    n = int(input())
    li = [j for j in range(n,0,-1)]
    if n%2==0:
        print(*li,sep=" ")
    else:
        mid = n//2
        li[mid],li[mid+1] = li[mid+1],li[mid]
        print(*li,sep=" ")