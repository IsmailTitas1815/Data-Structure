str = input()
str = str.lower()
str2 = ""

for i in str:
    if i!='a' and i!='e' and i!='i' and i!='o' and i!='u' and i!='y':
        str2+='.'
        str2+=i
print(str2)

