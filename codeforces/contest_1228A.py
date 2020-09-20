first,second = list(map(int,input().split()))
intFirst = int(first)
intSecond = int(second)

for i in range(intFirst,intSecond+1):
    currentFlag = 0
    strfirst = str(intFirst)
    strlen = len(strfirst)
    count = {}
    for i in range(strlen):
        count[strfirst[i]] = 0
    for i in range(strlen):
        if strfirst[i] in strfirst:
            count[strfirst[i]] += 1
    i=0
    while strfirst[i] is not None:
        if count[strfirst[i]] >1:
            currentFlag = -11
            flag = 11
            break
        else:
            i+=1

    if currentFlag ==0:
        print(strfirst)
        break











