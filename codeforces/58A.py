# str = input()
# li=[]
# str2 = ""
# lcount = 0
# for i in str:
#     if i not in li and (i=='h' or i=='e' or i=='l' or i=='o'):
#         li.append(i)
#     elif i=='l' and lcount<1:
#         li.append(i)
#         lcount+=1
# for i in li:
#     str2+= i
# if str2=="hello":
#     print("YES")
# else:
#     print("NO")

str = input()
presetStr = ['h','e','l','l','o']
count = 0
for i in str:
    if count<len(presetStr):
        if i == presetStr[count]:
            count+=1
    else:
        break
if count==len(presetStr):
    print("YES")
else:
    print("NO")