testcase = int(input())

for i in range(testcase):
    n = int(input())
    li = list(map(int,input().split()))[:n]
    s = set(li)
    if len(s)>1:
        print("YES")
        print(*li,sep=" ")
    else:
        print("NO")