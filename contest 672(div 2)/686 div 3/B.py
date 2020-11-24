for i in range(int(input())):
    n = int(input())
    li = list(map(int,input().split()))[:n]
    di = {}
    for j in li:
        if j in di:
            di[j] += 1
        else:
            di[j]=1
    keys = list(di.keys())
    val = list(di.values())
    selectedKeys = []
    for j in range(len(keys)):
        if val[j]==1:
            selectedKeys.append(keys[j])
    if len(selectedKeys)>0:
        indx = li.index(min(selectedKeys))
        print(indx+1)
    else:
        print(-1)