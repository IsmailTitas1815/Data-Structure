def firstOccurance(numbers, length, searchnum):
    answer = -1
    start = 0
    end = length - 1

    while start <= end:
        middle = (start + end) // 2

        if numbers[middle] == searchnum:
            answer = middle+1
            start = middle+1
        elif numbers[middle] > searchnum:
            end = middle - 1
            answer = middle
        else:
            start = middle + 1

    return answer

shopNum = int(input())
nums = list(map(int,input().split()))[:shopNum]
nums.sort()
for i in range(int(input())):
    sn = int(input())
    if sn<min(nums):
        print(0)
    elif sn>=max(nums):
        print(shopNum)
    else:
        ans = firstOccurance(nums, shopNum, sn)
        print(ans)