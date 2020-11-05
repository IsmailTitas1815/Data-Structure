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

# a, b = list(map(int, input().split()))
# a1 = list(map(int, input().split()))
# b1 = list(map(int, input().split()))
# amn = min(a1)
# bm = min(b1)
#
# amx = max(a1)
# if max(amn * 2, amx) < bm:
#     print(max(amn * 2, amx))
# else:
#     print(-1)