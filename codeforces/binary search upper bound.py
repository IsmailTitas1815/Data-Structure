def firstOccurance(numbers, length, searchnum):
    answer = -1
    start = 0
    end = length - 1

    while start <= end:
        middle = (start + end) // 2

        if numbers[middle] == searchnum:
            answer = middle
            start = middle + 1
        elif numbers[middle] > searchnum:
            end = middle - 1
        else:
            start = middle + 1

    return answer


nums = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 5, 5, 6, 6, 6, 7, 8]
tl = len(nums)
sn = 2

ans = firstOccurance(nums, tl, sn)
print(ans)