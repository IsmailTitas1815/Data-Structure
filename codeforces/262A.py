n,k = list(map(int,input().split()))
li = list(map(int,input().split()))[:n]
c=0
for i in li:
    i_str = str(i)
    count_4 = i_str.count('4')
    count_7 = i_str.count('7')
    total = count_4+count_7
    if total<=k:
        c+=1
print(c)
