# def tf(s,st):
#     f = 0
#     for j in s:
#         if j == st[f]:
#             f += 1
#             if f == len(st):
#                 break
#     if f == len(st):
#         return False
#     else:
#         return True
#
# for i in range(int(input())):
#     n = int(input())
#     s = input()
#     st = "trygub"
#     j = 1
#     while j<=n:
#         Lfirst = s[0: 1]
#         Lsecond = s[1:]
#         s = Lfirst+Lsecond
#
#     print(s)

for i in range(int(input())):
    n = int(input())
    s = input()
    s = list(sorted(s))
    print(*s,sep="")
