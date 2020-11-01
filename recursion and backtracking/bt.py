from itertools import permutations

li = [1,2,3,4]
print(*(list(permutations(li))),sep="\n")