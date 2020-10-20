for i in range(int(input())):
    n = input()
    l=len(n)
    d=int(n[0])
    s=0
    s+=(10*(d-1))
    if l==1:
        s+=1
    elif l==2:
        s+=3
    elif l==3:
        s+=6
    elif l==4:
        s+=10
    print(s)