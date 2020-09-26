s = input()
li = list(map(str,s))
listofV = ['A','E','I','O','U','Y']
count = 0
countli = []
l = len(li)
for i in range(l):
    if li[i] in listofV:
        count+=1
        countli.append(count)
        count=0

    elif i == l-1:
        count+=2
        countli.append(count)

    else:
        i+=1
        count+=1
print(max(countli))
