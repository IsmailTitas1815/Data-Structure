# from typing import List
#
#
# a = list(int(s) for s in Counter(a).keys())
# print(a)


class Solution:
    def removeDuplicates(self, nums):
        c=1
        for i in range(1,len(nums)):
            if nums[i-1] != nums[i]:
                nums[c] = nums[i]
                c+=1
        return c




nums = [1,1,1,1,2,2,2,2,3,3,4,5,5,6,6,6,7,7,7,8,8]
obj = Solution()
print(obj.removeDuplicates(nums))