testcase = int(input())
for i in range(testcase):
    li = list(map(int,input().split()))[:3]
    li.sort()
    if (li[1]==li[2]):
        print("YES")
        print(li[2],li[0],li[0])
    else:
        print("NO")