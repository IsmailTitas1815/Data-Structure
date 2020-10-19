for i in range(int(input())):
    a,b = list(map(int,input().split()))
    div = a%b
    if div == 0:
        print(0)
    else:
        print(b-div)