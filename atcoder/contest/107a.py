a,b,c = list(map(int,input().split()))
r = (a*(a+1)//2)*(b*(b+1)//2)*(c*(c+1)//2)
print(r%998244353)
