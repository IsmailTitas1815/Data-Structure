testcase = int(input())
for i in range(testcase):
    str = (input())
    l = len(str)
    tl = l
    li = []
    count = 0
    for j in range(l):
        if str[j] != "0":
            count +=1
            d = int(str[j])
            d = pow(10,tl-1)*d
            li.append(d)
            tl -= 1
        else:
            tl-=1
    print(count)
    print(*li, sep=" ")






