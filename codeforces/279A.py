n,t = list(map(int,input().split()))
li = list(map(int,input().split()))
count=0
s=0
lii=[]
i=0
while True:
    if i<n:

        if s+li[i]<=t:
            count+=1
            i+=1
        else:
            lii.append(count)
            s = s-li[i-count]
            if s+li[i]<=t:
                s = s+li[i]
                i+=1
            else:
                s = s - li[i - count]
                count = 0



