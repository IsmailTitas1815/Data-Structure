for i in range(int(input())):
    n = int(input())
    seat = n*4
    li = []
    for j in range(n):
        li.append(seat-2)
        seat-=2
    print(*li,sep=" ")