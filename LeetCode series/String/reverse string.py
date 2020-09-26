n = int(input())

if n<0:
    n = abs(n)
    s = str(n)
    s = ''.join(reversed(s))
    s= int(s)*-1
else:
    s = str(n)
    s = ''.join(reversed(s))
    s = int(s)
if -2147483648 < s <2147483647:
    print(s)
else:
    print(0)

# a = "82374"
# print(int(a[::-1]))
# 729,732,733,160,724,230,267,731B