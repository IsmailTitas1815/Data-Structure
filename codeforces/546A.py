k,n,w = list(map(int,input().split()))
s=0
for i in range(1,w+1):
    s+=(i*k)
if s>n:
    print(s-n)
else:
    print(0)