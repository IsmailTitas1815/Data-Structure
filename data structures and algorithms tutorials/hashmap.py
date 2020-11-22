class Hashmap:
    def __init__(self):
        self.max = 10
        self.arr = [[] for i in range(self.max)]
    def get_hash(self,key):
        h = 0
        for char in key:
            h+=ord(char)
        return h%self.max

    def __getitem__(self, key):
        hash = self.get_hash(key)
        return self.arr[hash]

    def __setitem__(self, key, val):
        hash = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[hash]):
            if len(element)==2 and element[0]==key:
                self.arr[hash][idx] = (key,val)
                found = True
                break
        if not found:
            self.arr[hash].append((key,val))


    def __delitem__(self, key):
        hash = self.get_hash(key)
        self.arr[hash] = None


a = Hashmap()
a["march 5"] = 120
a["march 6"] = 78
a["march 8"] = 67
a["march 9"] = 4
a["march 17"] = 459
print(a.arr)
print(a.get_hash('march 9'))
a.__delitem__('march 5')
print(a.arr)
print(a.__getitem__('march 6'))


# class HashTable:
#     def __init__(self):
#         self.MAX = 10
#         self.arr = [[] for i in range(self.MAX)]
#
#     def get_hash(self, key):
#         hash = 0
#         for char in key:
#             hash += ord(char)
#         return hash % self.MAX
#
#     def __getitem__(self, key):
#         arr_index = self.get_hash(key)
#         for kv in self.arr[arr_index]:
#             if kv[0] == key:
#                 return kv[1]
#
#     def __setitem__(self, key, val):
#         h = self.get_hash(key)
#         found = False
#         for idx, element in enumerate(self.arr[h]):
#             if len(element) == 2 and element[0] == key:
#                 self.arr[h][idx] = (key, val)
#                 found = True
#         if not found:
#             self.arr[h].append((key, val))
#
#     def __delitem__(self, key):
#         arr_index = self.get_hash(key)
#         for index, kv in enumerate(self.arr[arr_index]):
#             if kv[0] == key:
#                 print("del", index)
#                 del self.arr[arr_index][index]
#
#
#
# a = HashTable()
# a["march 6"] = 120
# a["march 6"] = 78
# a["march 8"] = 67
# a["march 9"] = 4
# a["march 17"] = 459
# print(a.arr)
