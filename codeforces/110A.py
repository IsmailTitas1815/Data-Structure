# def isLucky(n):
#     next_position = n
#
#     if isLucky.counter > n:
#         return 1
#     if n % isLucky.counter == 0:
#         return 0
#
#     next_position = next_position - next_position / isLucky.counter
#
#     isLucky.counter = isLucky.counter + 1
#
#     return isLucky(next_position)
#
# isLucky.counter = 2
#
# x = int(input())
# if isLucky(x):
#     print ("YES")
# else:
#     print ("NO")


#-------------------------above Lucky number----------------------------------------






n =input()
li = [i for i in n]
luckyli=['4','7']
length = len(li)
count = 0

if length==1:
    print("NO")
else:
    for i in li:
        if i in luckyli:
            count+=1
    if count==4 or count == 7:
        print("YES")
    else:
        print("NO")







