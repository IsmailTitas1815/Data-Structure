# a = int(input())
# print(bin(a)[2:])
# print(a)

# a = int(input(),2)
#
# print(a)
#
# print(bin(int(input())))
# print(bin(int(input())))
# print(bin(int(input())))
# print(bin(int(input())))


n,m,k = list(map(int,input().split()))
li = []
for i in range(m+1):
    li.append(int(input()))
friends = 0
for i in range(m):
    c=0
    xor = li[m]^li[i]
    str = (bin(xor))[2:]
    for j in str:
        # print(j)
        if j=='1':
            c+=1
    # print(c)
    if c<=k:
        friends+=1

print(friends)