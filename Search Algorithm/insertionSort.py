def insertion_sort(list):
    for i in range(1,len(list)):
        # for j in range(i-1,-1,-1): middle e -1 dewar reason hocche 0 index porjonto chalabo
        #     if list[j] > list[j+1]:
        #         list[j],list[j+1]= list[j+1],list[j]
            # else:
            #     break

        j = i-1
        while list[j] > list[j+1] and j>=0:
            list[j], list[j + 1] = list[j + 1], list[j]
            j-=1

list = [4,3,2,7,1,3,9,8]
insertion_sort(list)
print(list)