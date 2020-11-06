def sum(n):
    if n<10:
        return n
    return (n%10)+sum(n//10)
n = int(input())
print(sum(n))