testcase = int(input())

for i in range(testcase):
    n,m = list(map(int,input().split()))
    mainLi = []
    for j in range(n):
        li = list(map(int,input().split()))[:m]
        mainLi.append(li)

    print(mainLi)