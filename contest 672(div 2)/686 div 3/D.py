def isPrime(n):
    if (n <= 1):
        return False
    if (n <= 3):
        return True

    if (n % 2 == 0 or n % 3 == 0):
        return False

    i = 5
    while (i * i <= n):
        if (n % i == 0 or n % (i + 2) == 0):
            return False
        i = i + 6

    return True

import math

def primeFactors(n):
    li = []
    while n % 2 == 0:
        li.append(2)
        n = n / 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):

        while n % i == 0:
            li.append(i)
            n = n / i

    if n > 2:
        li.append(n)
    return li

for i in range(int(input())):
    n = int(input())
    if isPrime(n):
        print(n)
    else:
        li = primeFactors(n)





