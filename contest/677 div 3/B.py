t = int(input())
for i in range(t):
    n = int(input())
    li = list(map(int,input().split()))[:n]
    s=0
    li2 = []
    for j in range(len(li)):
        if li[j]==1:
            li2.append(j)
    if len(li2)>1:
        for k in range(1,len(li2)):
            s += (li2[k]-li2[k-1])-1
        print(s)

    else:
        print(0)


