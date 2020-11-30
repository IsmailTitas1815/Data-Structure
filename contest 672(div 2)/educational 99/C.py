for i in range(int(input())):
    a,b = list(map(int,input().split()))
    aw=bw=0
    if b+1 == a:
        a-=2
        aw+=1
    else:
        a-=1
    if a < 0 or a==0:
        a=0
        bw += b
    elif b < 0 or b==0:
        b=0
        aw += a
    while a>0 and b>0:
        a-=1
        b-=1
        if a==0:
            bw+=b
            break
        if b==0:
            aw+=a
            break
    print(aw,bw)


    # if b+1 == a:
    #     a-=2
    #     aw+=1
    # else:
    #     a-=1
    # while a!=0 and b!=0:
    #     if a>b:
    #         aw+=a-b
    #         a=b=0
    #     else:
    #         bw+=b-a
    #         a=b=0
    # print(aw,bw)

