# str = input()
# li = ['1','14','144']
# count=0
# i=2
# while count<len(str):
#     if str[i-2:i+1] in li:
#         count+=3
#         i+=3
#         print("if")
#         print("count:",count ,"i:",i)
#     elif str[i-2:i] in li:
#         count+=2
#         i+=2
#         print("elif1")
#         print("count:",count ,"i:",i)
#
#     elif str[i-2] in li:
#         count+=1
#         i+=1
#         print("elif2")
#         print("count:",count ,"i:",i)
#     else:
#         break
# print(count)
# if count==len(li):
#     print("YES")
# else:
#     print("NO")







str = input()
# li = ['1','14','144']
count=0
i=0
while count<len(str):
    if str[i:i+3] == "144":
        count+=3
        i+=3
        # print("if")
        # print("count:",count ,"i:",i)
    elif str[i:i+2] == "14":
        count+=2
        i+=2
        # print("elif1")
        # print("count:",count ,"i:",i)

    elif str[i] =='1':
        count+=1
        i+=1
        # print("elif2")
        # print("count:",count ,"i:",i)
    else:
        break
# print(count)
if count==len(str):
    print("YES")
else:
    print("NO")

