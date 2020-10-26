di = {}
for i in range(int(input())):
    str = input()
    if str in di:
        di[str]+=1
    else:
        di[str] = 1

m = max(di.values())

for key,value in di.items():
    if value==m:
        print(key)

# print(max(dict, key=dict.get))





















    # d = dict(Counter(str))
    # m = max(d.values())
    # for name,value in d.items():
    #     if value == m:
    # sort_orders = sorted(d.items(), key = lambda x:x[1])
    # sort_orders = sorted(d.items(), key=lambda x: x[1], reverse=True)
    # print(sort_orders)









# In[34]: dict.fromkeys(range(5), 0)
# Out[34]: {0: 0, 1: 0, 2: 0, 3: 0, 4: 0}
# In[35]: dict.fromkeys(['a', 'b', 'c'], 0)
# Out[35]: {'a': 0, 'b': 0, 'c': 0}