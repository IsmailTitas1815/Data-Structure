# import re
# s = '123 456-7890'
# new_s = [int(i) for i in re.findall('\d', s)]

# unformattedPhone = "1239084590348509 456-7890"
# numbersList = [int(s) for s in unformattedPhone if s.isdigit()]
# print(numbersList)

class Solution:
    def isHappy(self,num):
        setofvalue = set()
        while num!=1:
            num = sum(int(i)**2 for i in str(num))
            if num in setofvalue:
                return False
            setofvalue.add(num)
        return True


s=0
old = 0
num = int(input())
obj = Solution()
boo = obj.isHappy(num)
print(boo)
#
# def happy_numbers(n):
#     past = set()
#     while n != 1:
#         n = sum(int(i)**2 for i in str(n))
#         if n in past:
#             return False
#         past.add(n)
#     return True
# print([x for x in range(500) if happy_numbers(x)][:10])