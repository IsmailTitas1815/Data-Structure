n = int(input())
li = list(map(int,input().split()))[:n]
prog = []
progC = 0
math = []
mathC = 0
pe = []
peC = 0

for i in range(n):
    if li[i]==1:
        prog.append(i+1)
        progC+=1
    elif li[i]==2:
        math.append(i+1)
        mathC+=1
    elif li[i]==3:
        pe.append(i+1)
        peC+=1

teams = min(progC,mathC,peC)
print(teams)
for i in range(teams):
    print(prog[i],math[i],pe[i])
