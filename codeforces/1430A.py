for i in range(int(input())):
    n = int(input())
    if n<3 or n==4:
        print(-1)
    elif n%3==0:
        print(n//3,0,0)
    elif n%3==1:
        print((n//3)-2,0,1)
    elif n%3==2:
        print((n//3)-1,1,0)