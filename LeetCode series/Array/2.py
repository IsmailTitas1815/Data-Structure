# d = {'a':1,'b':8,'c':3,'d':4,'e':5}
# max = d[max(d.values())]
# max = d.get("a")
# print(max)


a_dictionary = {"a": 1, "b": 20, "c": 30}

# max_key = max(a_dictionary, key=a_dictionary.get)
# max = max(a_dictionary, key=a_dictionary.get)
# print(max)
# a = list(a_dictionary.values()).index(max(a_dictionary.values()))
# print(max(a_dictionary.values()))
# print(a)
# keys = list(a_dictionary.keys())
# vals = list(a_dictionary.values())
#
# m = keys[vals.index(max(vals))]
# print(m)

maximum = max(a_dictionary,key=a_dictionary.get )
print(maximum)