# def solveSudoku(bigArr, i, j):
#     if (i==len(bigArr)):
#         print("Here is the solution:")
#         for n in range(9):
#             print(*bigArr[n], sep=" ")
#     else:
#
#         ni = 0
#         nj = 0
#
#         if (j==len(bigArr[0])-1):
#             ni = i+1
#             nj = 0
#         else:
#             ni = i
#             nj = j+1
#
#         if (bigArr[i][j]!=0):
#             solveSudoku(bigArr,ni,nj)
#         else:
#             for k in range(1,10):
#                 if(isValid(bigArr,i,j,k)==True):
#                     bigArr[i][j]= k
#                     solveSudoku(bigArr,ni,nj)
#                     bigArr[i][j]=0
#
#
# def isValid(bigArr,x,y,val):
#     for l in range(9):
#         if (bigArr[x][l]==val):
#             return False
#     for l in range(9):
#         if(bigArr[l][y]==val):
#             return False
#
#     smi = (x//3)*3
#     smj = (y//3)*3
#     for i in range(3):
#         for j in range(3):
#             if (bigArr[smi+i][smj+j]==val):
#                 return False
#     return True
#
# bigArr = []
#
# for i in range(9):
#     li = list(map(int,input().split()))[:9]
#     bigArr.append(li)
#
# solveSudoku(bigArr,0,0)


# 0 0 0 0 6 5 9 2 8
# 1 0 5 0 2 0 7 6 0
# 0 0 2 8 0 0 0 0 0
# 5 3 0 4 8 9 0 0 0
# 6 4 0 7 0 0 8 3 0
# 0 0 7 0 1 0 0 4 9
# 4 9 0 0 0 8 1 5 7
# 0 1 8 0 0 0 3 0 0
# 0 0 0 0 9 1 2 0 0






def isValid(arr,x,y,val):

    for i in range(9):
        if arr[x][i]==val:
            return False

    for i in range(9):
        if arr[i][y] == val:
            return False

    smi = (x//3) *3
    smj = (y//3) *3

    for i in range(3):
        for j in range(3):
            if arr[smi+i][smj+j]==val:
                return False

    return True


def solveSudoku(arr,i,j):
    if (i==len(arr)):
        for n in range(9):
            print(*arr[n],sep=" ")
    else:

        ni = 0
        nj = 0

        if j==8:
            ni=i+1
            nj = 0
        else:
            ni = i
            nj = j+1


        if arr[i][j]!=0:
            solveSudoku(arr,ni,nj)
        else:
            for k in range(1,10):
                if (isValid(arr,i,j,k)==True):
                    arr[i][j]=k
                    solveSudoku(arr,ni,nj)
                    arr[i][j]=0

arr = []
for i in range(9):
    li = list(map(int,input().split()))[:9]
    arr.append(li)

solveSudoku(arr,0,0)