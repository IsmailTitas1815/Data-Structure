# for i in range(int(input())):
#     n = int(input())
#     count = 0
    # if n==1:
    #     print(0)
    # elif n%18!=3 and n%18!=0 and n%18!=9:
    #     print(-1)
    # else:
    #     while n>1:
    #         if n==1.5:
    #             count+=3
    #             break
    #         elif n==3:
    #             count+=2
    #             break
    #         else:
    #             if n%6==0:
    #                 n/=6
    #                 count+=1
    #             elif n%6==3:
    #                 n*=2
    #                 count+=1
    #     print(count)
#
# li = [1,3]
# li2 = [1]*10
# li.extend(li2)
# print(li)
#
#



for i in range(int(input())):
    n = int(input())
    count_2 = 0
    count_3 = 0

    while(n%2==0):
        n/=2
        count_2+=1
    while(n%3==0):
        n/=3
        count_3+=1
    if (n!=1 or count_2>count_3):
        print(-1)
    else:
        print(count_3+(count_3-count_2))














