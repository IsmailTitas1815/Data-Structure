# n,d = list(map(int,input().split()))
# money = []
# respect = []
# for i in range(n):
#     m,s = list(map(int,input().split()))
#     money.append(m)
#     respect.append(s)
# r = 0
# maximumRespect = max(respect)
# indx = respect.index(maximumRespect)
# val = money[indx]
#
# for i in range(n):
#     if 0<=abs(val-money[i])<d:
#         r+=respect[i]
# print(r)



n,d = list(map(int,input().split()))

li = []
for i in range(n):
    m,s = list(map(int,input().split()))
    li.append([m,s])

li.sort()
r = 0
c = 0
j=0
for i in li:
    c+=i[1]
    while i[0]-li[j][0]>=d:
        c-=li[j][1]
        j+=1
    r = max(r,c)

print(r)