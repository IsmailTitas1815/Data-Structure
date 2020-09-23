n = int(input())

for i in range(1,n+1):
    if n == 1:
        print("I hate it",end="")
    elif n%2!=0:
        if i==1:
            print("I hate that",end="")
        elif n==i:
            print(" I hate it", end="")
        elif i%2!=0:
            print(" I hate that",end="")
        else:
            print(" I love that",end="")
    elif n%2==0:
        if i==1:
            print("I hate that", end="")
        elif n==i:
            print(" I love it",end="")
        elif i%2!=0:
            print(" I hate that",end="")
        else:
            print(" I love that", end="")






