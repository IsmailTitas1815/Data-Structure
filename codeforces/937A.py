n = int(input())
li = set(map(int,input().split()))
if 0 in li:
    print(len(li)-1)
else:
    print(len(li))




# li = sorted(li)
# print(li)
# del li[:1]
# print(li)


# l = list(range(10))
# del l[:1]
# print(l)