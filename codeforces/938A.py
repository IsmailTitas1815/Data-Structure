n = int(input())
str = input()
str = list(str)
li = ['a','e','i','o','u','y']
l = len(str)
i=1
while i<len(str):
    if str[i-1] in li and str[i] in li:
        str.pop(i)
    else:
        i+=1
#
# for i in range(len(str)):
#     for j in range(i,len(str)):
#         if str[i] in li and str[j] in li:
#             str = str.replace(str[j],'',1)
#         else:
#             break

print(*str,sep="")
