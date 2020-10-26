# for i in range(int(input())):
#     a = input()
#     li0=0
#     li1=0
#     l=len(a)
#     for j in range(l):
#         if a[j]=='1':
#             li1+=1
#         else:
#             li0+=1
#
#     m = min(li1,li0)
#     pre0 = 0
#     pre1 = 0
#     for j in range(l):
#         if a[j] == '0':
#             pre0+=1
#         else:
#             pre1+=1
#
#         if a[j]=='0':
#             li0-=1
#         else:
#             li1-=1
#
#         m = min
#
#
#
#
#
#


for i in range(int(input())):
    n = input()
    l = len(n)
    c1 = []
    c2 = []
    o1 = 0
    o2 = 0

    for j in range(1, l + 1):
        if n[j - 1] == '1':
            o1 += 1
            c1.append(o1)
            c2.append(o2)
        else:
            o2 += 1
            c2.append(o2)
            c1.append(o1)
    r = 0
    print(c1)
    print(c2)
    li = []
    o11 = 0
    o20 = 0
    for k in range(l):
        if n[k] == '1':
            o11 += 1
        else:
            o20 += 1

        li.append(min(o20 + o1 - o11, o11 + o2 - o20))
    print(min(li))