# for i in range(int(input())):
#     n = int(input())
#     li = list(map(int,input().split()))[:n]
#     li2 = li.copy()
#     for j in range(n):
#         index = li2[j]
#         if index<len(li) and li[index-1]!=li[index]:
#             li[index-1]+=li[index]
#             li.pop(index)
#             # print(li)
#             # print("len",len(li))
#             # print(li2)
#         else:
#             # print("something")
#             continue
#     print(len(li))

for i in range(int(input())):
    n = int(input())
    li = list(map(int, input().split()))
    if len(set(li))>1:
        print(1)
    else:
        print(len(li))