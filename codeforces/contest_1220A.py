len = int(input())
str = input()
str = str.lower()
count = {}
c = 0
for i in range(len):
    count[str[i]] = c
for i in range(len):
    if str[i] == 'n':
        count[str[i]] += 1
    elif str[i] == 'z':
        count[str[i]] += 1
if str.find('n') != -1 and str.find('z') >=0:
    if count['n'] >= 1 and count['z'] >= 1:
        print(("1 " * count['n']) + ("0 "*count['z']).rstrip())
        # print(("1 " * count['n']).strip(), end="")
        # print((" 0"*count['z']).rstrip())
elif str.find('n') != -1:
    if count['n'] >=1:
        print(("1 " * count['n']).strip(), end="")
elif str.find('z') >=0:
    if count['z'] >= 1:
        print(("0 "*count['z']).rstrip())
