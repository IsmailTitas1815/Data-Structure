num = []
used = [0]*10

def perm(at,n):
    if at==n:
        for i in range(n):
            print(num[i],end=" ")
        return
    for i in range(1,n+1):
        if used[i]==0:
            num.insert(at,i)
            used[i]=1
            perm(at+1,n)
            used[i]=0
perm(0,3)
