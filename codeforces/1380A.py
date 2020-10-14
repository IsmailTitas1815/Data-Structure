for i in range(int(input())):
    n = int(input())
    li = list(map(int,input().split()))[:n]
    for j in range(1,n-1):
        if li[j-1]<li[j]>li[j+1]:
            print("YES")
            print(j,j+1,j+2)
            break
    else:
        print("NO")

