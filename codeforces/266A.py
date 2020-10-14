n = int(input())
count = 0
str = input()
max = 0
for i in range(1,n):
    if str[i] == str[i-1] and str[i]=='B':
        count+=1
        max = count
    elif str[i] == str[i-1]  and str[i]=='G':
        count+=1
        max = count
    elif str[i] == str[i-1]  and str[i]=='R':
        count+=1
        max = count

print(max)
