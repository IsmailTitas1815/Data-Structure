li = list(map(int,input().split()))
s = sum(li)
if s%5==0 and s!=0:
    print(int(s/5))
else:
    print("-1")