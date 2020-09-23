from math import ceil
testcase = int(input())

for i in range(testcase):
    k = 10
    count=0
    n = 0
    a,b = list(map(int, input().split()))
    if a==b:
        print(count)
    else:
        if a>b:
            max = a
            min = b
            diff = a-b
        else:
            max = b
            min = a
            diff = b-a

        count = diff // 10
        if diff%10 != 0:
            count+=1
        print(count)
