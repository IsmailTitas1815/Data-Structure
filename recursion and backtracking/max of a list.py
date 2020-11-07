def maximum(li,indx):
    if indx == len(li)-1:
        return li[indx]
    else:
        misa = maximum(li,indx+1)
        if misa>li[indx]:
            return misa
        else:
            return li[indx]

li = [2,3,545,64,23,423,423,423,5,345,32,45,3,545454,6,45,532,1]

print(maximum(li,0))