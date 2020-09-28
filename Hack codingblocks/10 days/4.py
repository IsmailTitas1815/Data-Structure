testcase = int(input())
for i in range(testcase):
    count= 0
    n  = int(input())
    b =(bin(n))[2:]
    for i in b:
        if i=='1':
            count+=1
    print(count)