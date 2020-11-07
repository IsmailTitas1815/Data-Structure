
#                          B = a^n


# def power(a,n):
#     if n==0:
#         return 1
#     elif n==1:
#         return a
#     else:
#         R = power(a,n//2)
#         if n%2==0:
#             return R*R
#         else:
#             return R*a*R
#
#
# print(power(5,26))
#
#





#                          B = (a^n)%m



def modpower(a,n,m):
    if n==1:
        return a%m
    elif n%2==0:
        return ((modpower(a,n//2,m)%m) * (modpower(a,n//2,m)%m))%m
    else:
        return ((modpower(a,n//2,m)%m) * (modpower(a,n//2,m)%m)*a)%m


ok = modpower(2,5,6)
print(ok)