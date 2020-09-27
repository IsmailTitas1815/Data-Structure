testcase = int(input())

for i in range(testcase):
    a,b = list(map(int,input().split()))
    count = 0
    while a>0 and b>0:
        if a>=b:
            vag = a//b
            count+=vag
            rem = a%b
            a = rem
        else:
            vag = b // a
            count += vag
            rem = b % a
            b=rem
    print(count)
