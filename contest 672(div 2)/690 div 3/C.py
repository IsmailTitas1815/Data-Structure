for i in range(int(input())):
    n = int(input())
    li=[]
    m=9
    if n>45 or n<0:
        print(-1)
    elif n==0:
        print(0)
    else:
        while n>0:
            if m<=n:
                li.append(m)
                n-=m
                m-=1
            else:
                m-=1
        li.sort()
        print(*li,sep="")


