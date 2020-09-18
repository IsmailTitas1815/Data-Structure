
pos = -1

def search(list,val):
    lowerbound = 0
    upperbound = len(list)-1
    global pos

    while lowerbound <= upperbound:
        mid = (lowerbound + upperbound) // 2
        if val == list[mid]:
            pos = mid
            return True
        else:
            if val > list[mid]:
                lowerbound = mid+1
            else:
                upperbound  = mid-1


list = [1,2,5,9,13,17,23,28,38,48,58,67,75,87,99]
val =int(input("Which number do you want to search: "))
# val = 13

if search(list,val):
    print("Found at position: ",pos+1)
else:
    print("Not found")



