s, n = list(map(int,input().split()))
f = True
strength = {}
for i in range(n):
    a,b = list(map(int,input().split()))
    if a in strength:
        strength[a] = strength.get(a)+b
    else:
        strength[a] = b

li = list(strength.keys())
li.sort()

for i in range(len(li)):
    if s>li[i]:
        s+=strength.get(li[i])
    else:
        f=False
        break
if f:
    print("YES")

else:
    print("NO")
