testcase = int(input())

# for i in range(testcase):
#     n = int(input())
#     li = list(map(int,input().split()))[:n]
#     count=0
#     for i in range(1, len(li)):
#         j = i
#         while j > 0 and li[j - 1] > li[j]:
#             li[j - 1], li[j] = li[j], li[j - 1]
#             j -= 1
#             count+=1
#     spin = ((n*(n-1))//2)-1
#     if count<=spin:
#         print("YES")
#     else:
#         print("NO")testcase = int(input())

for i in range(testcase):
    n = int(input())
    li = list(map(int,input().split()))[:n]
    count=0
    j = 0
    while j < len(li) - 1:
        print(li)
        print("J: ",j)
        if (li[j] > li[j + 1]):
            temp = li[j]
            li[j] = li[j + 1]
            li[j + 1] = temp
            count+=1
            j = -1
        j += 1 #if kaj korle eikhane ashei na. jodi if kaj na kore tobei eta kaj kore. kintu eita else er moto o na.
    spin = ((n*(n-1))//2)-1
    if count<=spin:
        print("YES")
    else:
        print("NO")


