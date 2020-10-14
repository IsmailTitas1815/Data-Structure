# testcase = int(input())
#
# for i in range(testcase):
#     n = int(input())
#     li = list(map(int, input().split()))[:n]
#     j = 1
#     count = 0
#     for j in range(len(li) - 1):
#         for k in range(j+1, len(li)):
#             if li[j] & li[k] >= li[j] ^ li[k]:
#                 count += 1
#     print(count)

testcase = int(input())

for i in range(testcase):
    n = int(input())
    li = list(map(int, input().split()))[:n]
    d={}
    for j in li:
        l = len(bin(j))
        if l in d:
            d[l]+=1
        else:
            d[l] =1
    res = 0

    for k in d:
        res += (d[k]*(d[k]-1))//2
    print(res)