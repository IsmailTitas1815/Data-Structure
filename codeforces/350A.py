n,m = list(map(int,input().split()))
success = set(map(int,input().split()))
success = list(success)
unsuccess = set(map(int,input().split()))
unsuccess = list(unsuccess)

mxSuccess = max(success)
minSuccess = min(success)
minUnSuccess = min(unsuccess)
f = False

if mxSuccess>minUnSuccess:
    print(-1)

else:
    while mxSuccess<minUnSuccess:
        if minSuccess*2<=mxSuccess:
            f = True
            break
        else:
            mxSuccess=minSuccess*2
    if f:
        print(mxSuccess)
    else:
        print(-1)


