from math import log,floor
n = int(input())
l = int(input())

ans = round(log(l,n),10)
print(ans)
f_ans = floor(ans)
if ans==f_ans:
    print("YES")
    print(int(ans-1))
else:
    print("NO")
