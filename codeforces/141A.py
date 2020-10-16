# a = [1,1,1,1,2,2,2,2,3,3,4,5,5,1,5,2,3,2,2]
# from itertools import groupby
# b= [len(list(group)) for key, group in groupby(a)]
# print(b)
import collections
str1 = input()
str2 = input()
str3 = input()
joinstr = str1+str2
count = 0
counter=collections.Counter(joinstr)
counter3=collections.Counter(str3)
if len((joinstr))!=len(str3):
    print("NO")
else:
    for i in counter:
        if counter[i] == counter3[i]:
            count = 0
        else:
            count = 1
            break

    if count == 0:
        print("YES")
    else:
        print("NO")
