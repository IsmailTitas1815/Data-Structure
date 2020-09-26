price , r = list(map(int,input().split()))
n=1
sum = price
while True:
    if sum%10==0 or sum%10==r:
        break
    else:
        sum= sum+price
        n+=1

print(n)
