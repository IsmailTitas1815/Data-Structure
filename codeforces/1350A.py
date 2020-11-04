import math
for i in range(int(input())):
    n,k = list(map(int,input().split()))
    paichi = False
    for j in range(k):
        if n%2==0:
            n+=(2*(k-j))
            break
        else:
            for a in range(3,math.floor(math.sqrt(n))+1,2):
                if n%a==0:
                    n+=a
                    paichi = True
                    break
                else:
                    paichi = False
            if paichi==False:
                n+=n
    print(n)
