for i in range(int(input())):
    n = int(input())
    li = list(map(int,input().split()))[:n]
    li.sort()
    count = 0
    if n==1:
        print("YES")
    else:
        for j in range(1,n):
            if li[j]- li[j-1] <=1:
                count =0
            else:
                count = 1
                break
        if count==0:
            print("YES")
        elif count ==1:
            print("NO")
            