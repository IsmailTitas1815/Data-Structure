testcase = int(input())
level = 0
for i in range(testcase):
    n  = int(input())
    count = 1
    while True:
        if level==0:
            count=0
            count+=1
            level+=2
        elif level<n:
            count+=1
            level+=2
        else:
            break
    print(count)
