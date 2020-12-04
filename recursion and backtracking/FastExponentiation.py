def power(a,N):
    if(N == 0):
        return 1
    elif(N%2==0):
        R = power(a,N / 2)
        return R*R
    else:
        return a*power(a,N-1)
a=5
for i in range(10):
    N = int(input())
    ans = str(power(a,N))
    print(ans[-2:])
