t =int(input())
for i in range(t):
    n = int(input())
    li = list(map(int,input().split()))
    l=len(li)
    m = max(li)
    if li[0] == m and li[0]!=li[1]:
        print(1)
    elif li[l-1] == m and li[l-2]!=m:
        print(l)
    else:
        for j in range(1,l-1):
            if li[j] == m and (li[j-1]<li[j] or li[j+1]<li[j]):
                print(j+1)
                break
        else:
            print(-1)

