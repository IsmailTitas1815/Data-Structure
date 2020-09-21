testcase  = int(input())
for i in range(testcase):
    n,a,b,c,d = list(map(int,input().split()))
    # if (c-d) <= n*(a-b) <= (c+d) or (c-d) <= n*(a+b) <= (c+d):
    if (n*(a+b) >= (c-d)) and (n*(a-b) <= (c+d)):
        print("YES")
    else:
        print("NO")
    # ABsum = a + b
    # ABsub = a - b
    #
    # CDsum = c + d
    # CDsub = c - d
    #
    # if ((n * ABsum >= CDsub) and (n * ABsub <= CDsum)):
    #     print("YES")
    # else:
    #     print("NO")
