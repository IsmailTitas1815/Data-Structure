s = input()
l = len(s)
li = [i for i in s[:l:2]]
li.sort()
plus = '+'
plus = plus.join(li)
print(plus)

# print("HEllo")