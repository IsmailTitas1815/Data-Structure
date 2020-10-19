n = int(input())
a = list(map(int,input().split()))
a.pop(0)
a = set(a)
b = list(map(int,input().split()))
b.pop(0)
b=set(b)

a|=b

if 0 in a:
    a.remove(0)
if len(a)==n:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")