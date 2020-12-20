for i in range(int(input())):
    n = int(input())
    k = n
    while True:
        s = str(k)
        res = k
        li = []
        c=0
        for j in s:
            if j not in li and j!='0':
                li.append(j)
        li_2 = [int(i) for i in li]
        length = len(li_2)
        for j in li_2:
            if k%j==0:
                c+=1
        if c==length:
            break
        else:
            k+=1
    print(res)