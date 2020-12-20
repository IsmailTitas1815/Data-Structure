testcase = int(input())
for i in range(testcase):
    n,k = list(map(int,input().split()))
    count=1
    # rem =0
    # if n>0:
    #     count+=1
    #     n=n-2
    # if n<k and n>0:
    #     count+=1
    # else:
    #     rem = n%k
    #     d = int((n-rem)/k)
    #     count+= d
    #     if rem!=0:
    #         count+=1
    # print(count)

    if n==1:
        print(1)
    else:
        for i in range(2,n,k):
            count+=1
        print(count)
