def catalan(li,n):
    for i in range(2,n+1):
        for j in range(0,i):
            li[i] += li[j]*li[i-j-1]
    return li[n]

n = int(input())
li = [0]*(n+2)
li[0] = 1
li[1] = 1
print(catalan(li,n))
