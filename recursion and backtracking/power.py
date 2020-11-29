def power(b,p):
    if b==0:
        return 1
    else:
        t = power(b,p/2)
        res = t*t
        





b , p = list(map(int,input()))
print(power(b,p))