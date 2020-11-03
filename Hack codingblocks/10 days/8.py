# for i in range(int(input())):
#     n =int(input())
#     li =list(map(int,input().split()))
#     c= 0
#     for j in range(n):
#         t=0
#         for k in range(j,n):
#             t += li[k]
#             if t%n==0:
#                 c+=1
#
#     print(c)


#                     PigeonHole Algorithm


for i in range(int(input())):
    n =int(input())
    li =list(map(int,input().split()))
    d = {}
    li2 = [0]*10000000
    liSumMod = []
    sum = 0
    for j in range(n):
        sum +=li[i]
        sum = (sum+n)%n
        

d = dict.fromkeys(range(1,10),0)
# if d[0] !=0:
#     d[0] = 1
print(d)
