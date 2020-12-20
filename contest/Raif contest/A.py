for i in range(int(input())):
    a,b,c,d = list(map(int,input().split()))
    if a==c:
        print(max(d,b)-min(d,b))
    elif b==d:
        print(max(a,c)-min(a,c))
    else:
        print((max(d,b)-min(d,b))+(max(a,c)-min(a,c))+2)
    # else:
    #     if a==c:
    #         print(b-d)
    #     elif b==d:
    #         print(a-c)
    #     else:
    #         print((a-c)+(b-d)+2)

#
# for i in range(int(input())):
#     li = list(map(int,input().split()))
#     li.sort()
#