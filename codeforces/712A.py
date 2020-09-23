testcase = int(input())
list = list(map(int, input().split()))[:testcase]
anotherList = []
for i in range(1,len(list)):
    anotherList.append(list[i-1]+list[i])
anotherList.append(list[len(list)-1])
print(*anotherList,sep=" ")