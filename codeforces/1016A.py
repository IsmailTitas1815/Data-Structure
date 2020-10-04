n,m = list(map(int,input().split()))
li = list(map(int,input().split()))[:n]
sum = 0
prev = 0
for i in range(len(li)):
    sum+=li[i]
    # print("step :",i+1)
    d = int(sum/m)
    # print("div :",d)
    count=d-prev
    # print("prev :",prev)
    # print("count(div-prev) :",count)
    prev+=count
    # print("sum =",sum)
    print(count)

# ok