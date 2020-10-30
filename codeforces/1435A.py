for i in range(int(input())):
    n = int(input())
    li = list(map(int,input().split()))[:n]
    li2 = []
    for j in range(len(li)-1,-1,-1):
        if j>=(len(li)//2):
           li2.append(li[j]*-1)
        else:
            li2.append(li[j])
    print(*li2,sep=" ")