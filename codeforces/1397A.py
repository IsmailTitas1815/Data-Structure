from collections import Counter
for i in range(int(input())):
    f = False
    di = dict()
    n = int(input())
    for j in range(n):
        li = list(input())
        counter = Counter(li)
        keys = list(counter.keys())
        values = list(counter.values())
        for k in range(len(keys)):
            if keys[k] not in di:
                di[keys[k]] = values[k]
            else:
                di[keys[k]] = di[keys[k]]+values[k]

    val = di.values()
    for p in val:
        if p%n==0:
            f = True
        else:
            f = False
            break

    if f:
        print("YES")
    else:
        print("NO")
