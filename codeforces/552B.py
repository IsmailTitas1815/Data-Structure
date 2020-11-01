n = input()
l = len(n)
intN = int(n)
total = 0
for i in range(l,0,-1):
    badDibo = intN - (pow(10,i-1)-1) # i tomo digit e koto gulo number ache
    total += badDibo*i  # jotogulo number ache tader lenth diye gun
    intN = intN-badDibo

print(total)