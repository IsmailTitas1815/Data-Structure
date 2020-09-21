testcase = int(input())

for i in range(testcase):
    n,a,b = list(map(int, input().split()))
    total_price = 0
    if n<2:
        total_price = a
    elif n>=2:
        if 2*a <= b:
            total_price = n*a
        elif 2*a > b:
            m = n//2
            if n%2==0:
                total_price += (m*b)
            elif n%2==1:
                total_price += (m * b) + a
    print(total_price)