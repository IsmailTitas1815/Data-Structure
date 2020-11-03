n,m = list(map(int,input().split()))
f = True
for i in range(1,n+1):
    if i%2!=0:
        print("#"*m)
    else:
        if f==True:
            print("."*(m-1)+"#")
            f=False
        else:
            print("#"+"."*(m-1))
            f=True

