n = int(input())
l=[]
if n%2==1:
    print(-1)
else:
    for i in range(1,n+1):
        l.append(i)
    l.reverse()
    print(*l,sep=" ")