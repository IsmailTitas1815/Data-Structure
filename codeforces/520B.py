from math import ceil
n,ex = list(map(int,input().split()))
count=0

while True:
    if ex < n:
        count+=n-ex
        print(count)
        break
    elif ex==n:
       print(count)
       break
    elif (n*2)<=ex:
       n*=2
       count+=1
    else:
       half = ceil(n/2)
       r = ex%n
       if r<=half and n>2:
           n=n-1
           count+=1
       else:
           n*=2
           count+=1



