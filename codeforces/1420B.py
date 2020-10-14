testcase = int(input())

for i in range(testcase):
    n = int(input())
    li = list(map(int, input().split()))[:n]
    j = 1
    count = 0
    for j in range(len(li) - 1):
        for k in range(1, len(li)):
            if j < k:
                # print(f"li[j]= {li[j]} li[k]= {li[k]}")
                jnot = ~li[j]
                knot = ~li[k]
                andOP = li[j] & li[k]
                # print("j=",j)
                # print("and",andOP)
                xorOP = li[j] & knot | li[k] & jnot
                # print("Xor",xorOP)
                if andOP >= xorOP:
                    count += 1
    print(count)

#
# a = 4
# b=7
#
# print(a&b)
# anot = ~a
# bnot = ~b
#
# print(a&bnot | b&anot)