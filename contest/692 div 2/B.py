# for i in range(int(input())):
#     n = int(input())
#     k = n
#     while True:
#         s = str(k)
#         res = k
#         li = []
#         c=0
#         for j in s:
#             if j not in li and j!='0':
#                 li.append(j)
#         li_2 = [int(i) for i in li]
#         length = len(li_2)
#         for j in li_2:
#             if k%j==0:
#                 c+=1
#         if c==length:
#             break
#         else:
#             k+=1
#     print(res)


#
# for i in range(int(input())):
#     n = int(input())
#     k = n
#     while k>0:
#        vag = k%10
#        if vag>1:
#            if n%vag==0:
#                k = k // 10
#            else:
#                n+=1
#                k=n
#        else:
#            k//=10
#
#     print(n)









# def digit(n,a):
#     if a==0:
#         return True
#     return ( a!=0 and n%a==0)
#
# def allDigits(n):
#     k = n
#     while k>0:
#         vag = k%10
#         if not digit(n,vag):
#             return False
#         k//=10
#     return True
#
#
# for i in range(int(input())):
#     n = int(input())
#     k = n
#     while True:
#         if allDigits(n):
#             print(n)
#             break
#         else:
#             n+=1


#not ok

#
# for i in range(int(input())):
#     n = int(input())
#     s = str(n)
#     if len(s)>4:
#         s1 = s[0:len(s)-5]
#         s2 = s.replace(s1,"")
#         print(s1,s2)
#         n= int(s2)
#     k = n
#     while k > 0:
#         vag = k % 10
#         if vag > 1:
#             if n % vag == 0:
#                 k = k // 10
#             else:
#                 n += 1
#                 k = n
#         else:
#             k //= 10
#
#     if len(s) > 4:
#         n = s1 + str(n)
#         print(int(n))
#     else:
#         print(n)
#
#


