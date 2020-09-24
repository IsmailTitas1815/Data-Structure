
def sortArrays(arr):
    length = len(arr)

    j = 0
    count=0

    while j < length - 1:

        if (arr[j] > arr[j + 1]):
            count+=1
            temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = temp
            j = -1
        j += 1
    print(count)
    return arr
if __name__ == '__main__':
    arr = [5,3,2,1,4]
    print("Original array: ", arr)
    arr = sortArrays(arr)

    print("Sorted array: ", arr)