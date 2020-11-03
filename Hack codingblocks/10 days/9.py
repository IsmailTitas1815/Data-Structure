# from nltk.tokenize import word_tokenize


def extractStringAtKey(st,key):
    st = st.split(" ")
    return st[key-1]



n = int(input())
arr = []
keyList = {}
for i in range(n):
    st = input()
    arr.append(st)

key , boo , ordr = list(map(str,input().split()))
key = int(key)

for i in arr:
    keyList[i] = extractStringAtKey(i,key)

if ordr == "numeric":
    keyList = sorted(keyList)
else:
    print()