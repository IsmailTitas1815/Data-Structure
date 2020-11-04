task, time = list(map(int,input().split()))
baki = 240 - time
count = 0
total = 0

for i in range(1,task+1):
    total+=(i*5)
    if total<=baki:
        count+=1
    else:
        break
print(count)