n,m,k,s = list(map(int,input().split()))

for i in range(n):
    li = list(map(str,input().split()))[:m]
    for j in range(m):
        if s<k:
            break
        elif li[j] == '#':
            break
        elif li[j] == '.':
            if j==n-1:
                s-=2
            else:
                s-=3
        elif li[j] == '*':
            if j==n-1:
                s+=5
            else:
                s+=4
    if s < k:
        break
if s>=k:
    print("Yes")
    print(s)
else:
    print("No")