testcase = int(input())
for i in range(testcase):
    stick = 1
    coal = 0
    count = 0
    a,b,c = list(map(int , input().split()))

    # while True:
    #     stick = stick+a-1
    #     count+=1
    #     stick = stick - b
    #     coal += 1
    #     count+=1
    #     break
    # print(count)


    while True:
        if stick - (b*c) >= c:
            break
        stick = stick+a-1
        count += 1
    print(count+c)