import bisect

m , n = list(map(int,input().split()))
li1 = list(map(int,input().split()))
li1.sort()
li2 = list(map(int,input().split()))

for i in li2:
    print(bisect.bisect(li1,i),end=" ")
