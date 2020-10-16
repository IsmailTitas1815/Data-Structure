# t = int(input())
# li = list(map(int,input().split()))[:t]
# li2=[]
#
# for i in range(len(li)):
#     if i==len(li)-1:
#         li2.insert(li[0]-1,li[len(li)-1])
#     else:
#         li2.insert(li[i+1]-1,li[i])
# print(*li2,sep=" ")
#
import collections
# sorted_dict = collections.OrderedDict(di)
# print(sorted_dict)

t = int(input())
li = list(map(int,input().split()))[:t]
di = {key for key in enumerate(li,1)}
di = dict(di)
di = {k: v for k, v in sorted(di.items(), key=lambda a: a[1])}
print(*di.keys(),sep=" ")


