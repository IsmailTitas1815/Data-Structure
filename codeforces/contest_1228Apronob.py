first , second = list(map(int, input().split()))
found_list = []
for i in range(first,second+1):
    flag = 1
    current = i
    li = []
    while current !=0 :
        d = current%10
        if d in li:
            flag = 0
            break
        li.append(current%10)
        current = current//10
    if flag == 1:
        found_list.append(i)

if len(found_list) > 0:
    print(found_list[0])
else:
    print("-1")


#-----------------------------------------------------

# def repeated_digit(n):
#     a = []
#     while n != 0:
#         d = n % 10
#         if d in a:
#             return 0
#
#         a.append(d)
#         n = n // 10
#
#     return 1
#
# l=[]
# a,b = list(map(int, input().split()))
# for i in range(a,b+1):
#     n=i
#     if repeated_digit(n) is 1:
#         l.append(i)
#
# if len(l) > 0:
#     print(l[0])
# else:
#     print('-1')







# a,b = list(map(int, input().split()))
#
# n_li = []
# for i in range(a,b+1):
#     f = 1
#     dig = i
#     li = []
#
#     while dig!=0:
#         if dig%10 in li:
#             f = 0
#             break
#         else:
#             li.append(dig % 10)
#             dig = dig//10
#
#     if f == 1:
#         n_li.append(i)
#
# if len(n_li)>0:
#     print(n_li[0])
# else:
#     print('-1')