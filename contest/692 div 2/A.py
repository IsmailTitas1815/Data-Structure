for i in range(int(input())):
    n = int(input())
    s = input()
    s = s[::-1]
    if n%2==0:
        m = n/2
    else:
        m = n//2
    c = 0

    for j in s:
        if j==')':
            c+=1
        else:
            break

    if c>m:
        print("YES")
    else:
        print("NO")