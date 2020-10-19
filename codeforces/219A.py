# import collections
# n = int(input())
# s=input()
# di = collections.Counter(s)
# print(di)
# s = set(di.values())
# if len(s)>1:
#     print(-1)
# else:
#     li = list(di.keys())
#     li*=sum(s)
#     print(*li,sep="")

n = int(input())
s=input()
s = sorted(s)
s = "".join([str(i) for i in s])
s2 = s[::n]*n
s3 = sorted(s2)
s3 = "".join([str(i) for i in s3])
if s3!=s:
    print(-1)
else:
    print(s2)