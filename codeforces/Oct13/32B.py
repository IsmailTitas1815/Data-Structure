str = input()
str2 = ""
print(str2)
i=1
while i<=len(str):
    if str[i-1]=='-' and str[i]=='-':
        str2+='2'
        i+=2
    elif str[i-1]=='-' and str[i]=='.':
        str2+='1'
        i+=2
    elif str[i-1]=='.':
        str2+='0'
        i+=1

print(str2)