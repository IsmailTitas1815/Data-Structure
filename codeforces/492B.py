n , l  = list(map(int,input().split()))
li = list(map(int,input().split()))[:n]
li.sort()
li2= []
if len(li) == 1:
    if li[0]==0 or li[0]==l:
        print(format(l,'.10f'))
    else:
        beforediff = li[0]-0
        afterdiff = l-li[0]
        print(format(max(afterdiff,beforediff),'.10f'))
else:
    for i in range(len(li)):
        if i==0:
            if li[i]==0:
                afterdiff = (li[i+1]-li[i])/2
                li2.append(afterdiff)
            else:
                beforediff = (li[i]-0)
                afterdiff = (li[1]-li[0])/2
                li2.append(max(beforediff,afterdiff))
        elif i==len(li)-1:
            if li[i]==l:
                beforediff = (li[i]-li[i-1])/2
                li2.append(beforediff)
            else:
                afterdiff = l - li[i]
                beforediff = (li[i]-li[i-1])/2
                li2.append(max(beforediff,afterdiff))
        else:
            beforediff = (li[i] - li[i-1])/2
            afterdiff = (li[i+1] - li[i])/2
            li2.append(max(beforediff,afterdiff))

    print(format(max(li2),'.10f'))
