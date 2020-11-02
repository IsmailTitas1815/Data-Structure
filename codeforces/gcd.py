def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

a,b = list(map(int,input().split()))
print(gcd(a,b))
#                                  same work
def gcd(a,b):
    if a%b==0:
        return b
    else:
        return gcd(b,a%b)

a,b = list(map(int,input().split()))
print(gcd(a,b))