
a1, a2, b1, b2, k = list(map(int, input().split()))
if a2<b1:
    print(0)
elif a1==a2 or b1 == b2:
    if a1==k or b1==k:
        print(0)
    else:
        print(1)
elif (a1>b1 and a1>b2) or (b1>a1 and b1>a2):
    print(0)

elif  b2>=a1>=b1:
    if a2>=b2:
        if a1<=k<=b2:
            print(b2-a1)
        else:
            print(b2-a1+1)
    else:
        if a1<=k<=a2:
            print(a2-a1)
        else:
            print(a2-a1+1)
elif b2 >= a2 >= b1:
    if a1 >= b1:
        if a1 <= k <= a2:
            print(a2 - a1)
        else:
            print(a2 - a1 + 1)
    else:
        if b1 <= k <= a2:
            print(a2 - b1)
        else:
            print(a2 - b1 + 1)

elif a1<=b1<=a2:
    if b2>=a2:
        if a2>=k>=b1:
            print(a2-b1)
        else:
            print(a2-b1+1)
    else:
        if b2>=k>=b1:
            print(b2-b1)
        else:
            print(b2-b1+1)
elif a1<=b2<=a2:
    if b1>=a1:
        if b2>=k>=b1:
            print(b2-b1)
        else:
            print(b2-b1+1)
    else:
        if b2>=k>=a1:
            print(b2-a1)
        else:
            print(b2-a1+1)


else:
    if b1<=k<=a2:
        print(b1-a2)
    else:
        print(b1-a2+1)