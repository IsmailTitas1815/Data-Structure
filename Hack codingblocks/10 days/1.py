n = int(input())
div2 = n//2
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1:
            if j==1 or j>div2:
                print("*",end="")
            else:
                print(" ",end="")
        elif i>1 and i<=div2:
            if j==1 or j==div2+1:
                print("*",end="")
            else:
                print(" ",end="")
        elif i==div2+1:
            print("*",end="")
        elif i>div2 and i<n:
            if j==div2+1 or j==n:
                print("*",end="")
            else:
                print(" ",end="")
        elif i==n:
            if j<=div2+1 or j==n:
                print("*",end="")
            else:
                print(" ",end="")
    print("\n")