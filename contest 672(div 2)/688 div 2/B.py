from math import floor
# def firstOccurance(numbers, length, searchnum):
#     answer = -1
#     start = 0
#     end = length - 1
#
#     while start <= end:
#         middle = (start + end) // 2
#
#         if numbers[middle] == searchnum:
#             answer = middle
#             end = middle - 1
#         elif numbers[middle] > searchnum:
#             end = middle - 1
#         else:
#             start = middle + 1
#
#     return answer


t = int(input())
for i in range(t):
    n = int(input())
    li = list(map(int,input().split()))
    li.sort()
    av = floor(sum(li)/n)
    if av in li:
        pin = av
    else:
        for j in range(len(li)):
            if li[j]>av and j==0:
                pin = li[0]
                break
            elif li[j]>av and j>0:
                pin = li[j-1]
                break

    print(pin)




    # nums = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 5, 5, 6, 6, 6, 7, 8]
    # tl = len(nums)
    # sn = 2
    #
    # ans = firstOccurance(nums, tl, sn)
    # print(ans)