testcase = int(input())

for i in range(testcase):
    n = int(input())
    a = 0
    fa = 1
    while n>0:
        if n%2==0:
            if fa ==1:
                a += n//2
                fa=0
                n -= n//2
            else:
                n -= n//2
                fa=1
        else:
            if fa ==1:
                a += 1
                fa = 0
                n -= 1
            else:
                n -= 1
                fa=1
    print(a)
