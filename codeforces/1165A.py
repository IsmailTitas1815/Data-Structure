n = int(input())

for i in range(1,n+1):
    if i == 1:
        print("I hate it",end="")
    else:
        if i%2!=0:
            print(" I hate it",end="")
        else:
            print(" I love it",end="")