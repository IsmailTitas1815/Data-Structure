ali=[]
bli=[]
for i in range(int(input())):
    a,b = list(map(int,input().split()))
    ali.append(a)
    bli.append(b)
c=0
for i in range(len(ali)):
    for j in range(len(ali)):
        if ali[i] == bli[j]:
            c+=1

print(c)
