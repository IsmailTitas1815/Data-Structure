max = 0
sum =0
for i in range(int(input())):
    a,b = list(map(int,input().split()))
    sum += b-a
    if sum>max:
        max = sum
print(max)