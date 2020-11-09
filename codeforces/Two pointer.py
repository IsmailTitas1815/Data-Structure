#                           Two sum

li = [1,2,456,3,5,6,4,6,8,3,9,11,6,31,6,3,9,0,12,25,19,20,25,40,41]
li.sort()
print(li)
n = 50
i = 0
j = len(li)-1
while li[i]+li[j]!=n:
    if li[i]+li[j]>n:
        j-=1
    else:
        i+=1

print(i,j)





#                   wanted difference



# li = [456,3,5,6,4,6,8,3,9,11,6,31,6,3,9,12,25,19,20,25,40,41]
# li.sort()
# print(li)
# diff = 5
# i = 0
# j = len(li)-1
# while li[j]-li[i]!=diff:
#     if li[j]-li[i]>diff:
#         j-=1
#     else:
#         i+=1
#
# print(i,j)