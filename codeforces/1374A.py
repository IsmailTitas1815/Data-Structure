for i in range(int(input())):
    x,y,n = list(map(int,input().split()))
    count = 0
    while n>=0:
        # if n%x==y:
        #     if count==0:
        #         print(n)
        #         break
        #     else:
        #         print(n-x)
        #         break
        # else:
        #     n+=(y - (n%x))
        #     count+=1

        rem = n%x
        if rem==y:
            print(n)
            break
        elif rem>y:
            print(n-(rem-y))
            break
        elif rem<y:
            print(n+(y-rem)-x)
            break

        # rem = n%x
# print(12346%7)