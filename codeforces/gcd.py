# def gcd(a,b):
#     if b==0:
#         return a
#     else:
#         return gcd(b,a%b)
#
# a,b = list(map(int,input().split()))
# print(gcd(a,b))
# #                                  same work
# def gcd(a,b):
#     if a%b==0:
#         return b
#     else:
#         return gcd(b,a%b)
#
# a,b = list(map(int,input().split()))
# print(gcd(a,b))

def gcd(u, v):
    """ This function will calcluate
    GCD of given two numbers.
    If the input is negative, both the
    numbers are converted to positive
    before the calculation
    """
    if u == v:
        return u
    elif u == 0:
        return v
    elif v == 0:
        return u
    # u is even
    elif u & 1 == 0:
        # v is even
        if v & 1 == 0:
            return 2*gcd(u >> 1, v >> 1)
        # v is odd
        else:
            return gcd(u >> 1, v)
    # u is odd
    elif u & 1 != 0:
        # v is even
        if v & 1 == 0:
            return gcd(u, v >> 1)
        # v is odd and u is greater than v
        elif u > v and v & 1 != 0:
            return gcd((u-v) >> 1, v)
        # v is odd and u is smaller than v
        else:
            return gcd((v-u) >> 1, u)

print(gcd(10,6))
