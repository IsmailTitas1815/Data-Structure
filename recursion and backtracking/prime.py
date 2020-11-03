def prime(n,half):
    if half==1:
        return 1
    if n%half==0:
        return 0

    return prime(n,half-1)

n = int(input())
half = n//2
res = prime(n,half)

if res==1:
    print("YES")
else:
    print("NO")