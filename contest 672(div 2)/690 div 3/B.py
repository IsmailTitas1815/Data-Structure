for i in range(int(input())):
    n = int(input())
    s = input()
    if n>=4:
        if s[0]=='2' and s[1]=='0' and s[2]=='2' and s[3]=='0':
            print("YES")
        elif s[0]=='2' and s[1]=='0' and s[2]=='2' and s[n-1]=='0':
            print("YES")
        elif s[0]=='2' and s[1]=='0' and s[n-2]=='2' and s[n-1]=='0':
            print("YES")
        elif s[0] == '2' and s[n-3]=='0' and s[n-2]=='2' and s[n-1]=='0':
            print("YES")
        elif s[n-4]=='2' and s[n-3]=='0' and s[n-2]=='2' and s[n-1]=='0':
            print("YES")
        else:
            print("NO")
    else:
        print("NO")