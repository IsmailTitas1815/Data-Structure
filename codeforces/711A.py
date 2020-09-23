testcase = int(input())
count = 0
li = []
for i in range(testcase):
    str = input()
    if "OO" in str:
        count+=1
        if count ==1:
            str = str.replace("OO","++",1)
            print("YES")
    li.append(str)

if count==0:
    print("NO")
else:
    print(*li,sep="\n")

