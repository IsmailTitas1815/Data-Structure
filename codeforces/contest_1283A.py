t = int(input())

for i in range(t):
    hour,min = list(map(int , input().split()))
    total_min = 60 - min
    hour +=1
    while hour<24:
        total_min+=60
        hour+=1

    print(total_min)