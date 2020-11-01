t = int(input())
for i in range(t):
    n,x = list(map(int,input().split()))
    li = list(map(int,input().split()))[:n]
    li2 = list(map(int,input().split()))[:n]
    if i<(t-1):
        faltu = input()
    li.sort()
    li2.sort(reverse=True)
    f = True
    for j in range(n):
        if (li[j]+li2[j]>x):
            f = False
            break
        else:
            f = True

    if f:
        print("Yes")
    else:
        print("No")


# 4
# 3 4
# 1 2 3
# 1 1 2
# 2 6
# 1 4
# 2 5
# 4 4
# 1 2 3 4
# 1 2 3 4
# 1 5
# 5
# 5
