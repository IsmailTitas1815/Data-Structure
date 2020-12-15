for i in range(int(input())):
    n = int(input())
    li = list(map(int,input().split()))[:n]
    c=0
    while len(set(li))!=1:
        if li[0]<li[len(li)-1]:
            li[0]+=li[1]
            li.pop(1)
            c+=1
        else:
            li[len(li)-2]+=li[len(li)-1]
            li.pop(len(li)-1)
            c+=1
    print(c)