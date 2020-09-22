testcase = int(input())
length = []
li= list(map(int,input().split()))[:testcase]

# for i in range(len(li)):
#     count = 1
#     for j in range(i+1,len(li)):
#         if li[j-1] < li[j]:
#             count+=1
#         else:
#             break
#     length.append(count)
#
# print(max(length))
# print(li)
# for i in range(testcase):
#     length.append(1)
count = 1
oldcount = 0
if len(li)==1:
    print(1)
else:
    for i in range(1,testcase):
        oldcount = 0
        if li[i-1] < li[i]:
            count+=1
            oldcount = count
        else:
            count=1

        if oldcount >= count:
            length.append(oldcount)
        else:
            length.append(count)

    print(max(length))