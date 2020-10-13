# def find_gcd(x, y):
#     while (y):
#         x, y = y, x % y
#
#     return x
#
# testcase = int(input())
#
# for j in range(testcase):
#
#     l = [i for i in range(1,int(input())+1)]
#     print(l)
#
#     num1 = l[0]
#     num2 = l[1]
#     gcd = find_gcd(num1, num2)
#     for i in range(2, len(l)):
#         gcd = find_gcd(gcd, l[i])
#         print(gcd)
#

for i in range(1,int(input())+1):
    print(int(input())//2)
    