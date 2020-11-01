n,ex = list(map(int,input().split()))
count=0

if ex<n:
    print(n-ex)
else:
    ex,n = n,ex
    while True:
        if n<ex or n==ex:
            count+=(ex-n)
            print(count)
            break
        elif n%2==0:
            n//=2
            count+=1
        elif n%2!=0:
            n+=1
            count+=1



