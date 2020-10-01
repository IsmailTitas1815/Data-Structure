testcase = int(input())

for i in range(testcase):
    n = int(input())
    a = list(map(int,input().split()))[:n]
    b = list(map(int,input().split()))[:n]
    c = list(map(int,input().split()))[:n]
    li =[]
    k=0
    for j in range(n):
        if j==0:
            li.append(a[j])
            print(f"j = {j}, li[{j}] = {li[j]}")
            j+=1
        print("something 1")
        while a[j] != li[j - 1]:
            if j>=n:
                break
            else:
                li.append(a[j])
                print(f"j = {j}, li[{j}] = {li[j]}")
                j = j + 1
                print("now j =", j)
        print("something 2")
        while b[j] != li[j - 1]:
            if j >= n:
                break
            else:
                li.append(b[j])
                print(f"j = {j}, li[{j}] = {li[j]}")
                j = j + 1
                print("now j =", j)
        print("something 3")

        while c[j] != li[j - 1]:
            if j >= n:
                break
            else:
                li.append(c[j])
                print(f"j = {j}, li[{j}] = {li[j]}")
                j = j + 1
                print("now j =", j)
        print("j =",j)

    print(*li,sep=" ")


    # for j in range(n):
    #     li.append(a[j])
    #     j+=1
    #     if a[j] != li[j-1]:
    #         li.append(a[j])
    #     elif b[j] != li[j-1]:
    #         li.append(b[j])
    #     elif c[j] != li[j-1]:
    #         li.append(c[j])
    # print(*li,sep=" ")


#
#     for j in range(n):
#         count=0
#         oldcount = 0
#         if j==0:
#             li.append(a[j])
#         print("something 1")
#         while a[j] != li[j-1]:
#             if j >= n:
#                 break
#             else:
#                 li.append(a[j])
#                 print(f"j = {j}, li[{j}] = {li[j]}")
#                 count+=1
#                 oldcount = count
#         j+=oldcount
#         count=0
#         while b[j] != li[j-1]:
#             if j >= n:
#                 break
#             else:
#                 li.append(b[j])
#                 print(f"j = {j}, li[{j}] = {li[j]}")
#                 count += 1
#                 oldcount = count
#         j += oldcount
#         count = 0
#         print("something 3")
#
#         while c[j] != li[j-1]:
#             if j >= n:
#                 break
#             else:
#                 li.append(c[j])
#                 print(f"j = {j}, li[{j}] = {li[j]}")
#                 count += 1
#                 oldcount = count
#         j += oldcount
#         count = 0
#
#         print("Last j = ",j)
#         if j>=n:
#             break
#     print(*li,sep=" ")
#
# def a():

