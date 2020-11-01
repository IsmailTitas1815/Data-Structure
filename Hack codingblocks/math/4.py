for i in range(int(input())):
    n = int(input())
    li1 = list(map(int,input().split()))[:n]
    li2 = list(map(int,input().split()))[:n]
    res = 0
    for j in range(n-1):
        for k in range(j+1,n):
            res += (abs(li1[j]-li1[k])* max(li2[j],li2[k]))

    print(res)