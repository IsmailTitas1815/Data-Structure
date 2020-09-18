def countEmerald(a, b):
    count = -1
    mi = min(a, b)
    ma = max(a, b)

    if mi == 0 or ma == 0:
        count = 0
        return count

    elif ma >= (2 * mi):
        count = mi
        return count
    else:
        count = (mi + ma) // 3
        return count


n = int(input())

for i in range(n):
    a, b = list(map(int, input().split()))
    numofEmerald = countEmerald(a, b)
    print(numofEmerald)