from itertools import groupby
class Solution:
    def singleNumber(self, List):
        List.sort()
        import collections
        count = collections.Counter(List)
        keylist = list(count.keys())
        vallist = list(count.values())
        for i in range(len(vallist)):
            if vallist[i] == 1:
                return keylist[i]
obj = Solution()
li = [2,2,1]
obj.singleNumber(li)

# a = [1,1,1,1,2,2,2,2,3,3,4,5,5]
# counter = [len(list(group)) for key, group in groupby(a)]
# print(counter)
# print(c)




# a = [1,1,1,1,2,2,2,2,3,3,4,5,5]
# from itertools import groupby
# c=[len(list(group)) for key, group in groupby(a)]



import collections
# a = [1,1,1,1,2,2,2,2,3,3,4,5,5]
# count=(collections.Counter(a))
# print(count)
# Counter({1: 4, 2: 4, 3: 2, 5: 2, 4: 1})
# print(count.values())
# [4, 4, 2, 1, 2]
# print(count.keys())
# [1, 2, 3, 4, 5]
# print(count.most_common(3))
# [(1, 4), (2, 4), (3, 2)]