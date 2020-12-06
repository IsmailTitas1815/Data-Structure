for i in range(int(input())):
    n = int(input())
    li = list(map(int,input().split()))
    # posLi = []
    # negLi = []
    # zeros = []
    # for j in li:
    #     if j==0:
    #         zeros.append(j)
    #     elif j<0:
    #         negLi.append(j)
    #     else:
    #         posLi.append(j)
    # l = len(posLi) if len(posLi) < len(negLi) else len(negLi)
    if sum(li)==0:
        print("NO")
    else:
        s = sum(li)
        if s>0:
            print("YES")
            li.sort(reverse=True)
            print(*li,sep=" ")
        else:
            print("YES")
            li.sort()
            print(*li,sep=" ")













    # if sum(li)==0:
    #     print("NO")
    # else:
    #     print("YES")
    #     print(*posLi,sep=" ")

