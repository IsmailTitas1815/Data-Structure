testcase = int(input())
num = list(map(int,input().split()))[:testcase]
l = len(num)
countofOne = 0
if l==1:
    if num[0] == 0:
        print("NO")
    else:
        print("YES")
else:
    for i in range(l):
        if num[i] == 1:
            countofOne+=1
    if countofOne == l-1:
        print("YES")
    else:
        print("NO")
