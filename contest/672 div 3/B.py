#
# def transpose(mat, tr, N):
#     for i in range(N):
#         for j in range(N):
#             tr[i][j] = mat[j][i]
#
#
# def isSymmetric(mat, N):
#     tr = [[0 for j in range(len(mat[0]))] for i in range(len(mat))]
#     transpose(mat, tr, N)
#     for i in range(N):
#         for j in range(N):
#             if (mat[i][j] != tr[i][j]):
#                 return False
#     return True
# mat = [[1, 3, 5], [3, 2, 4], [5, 4, 1]]
# if (isSymmetric(mat, 3)):
#     print("Yes")
# else:
#     print("No")

# testcase = int(input())
# for i in range(testcase):
#     n,m = list(map(int,input().split()))
#     matrix = []
#
#     for j in range(2):
#
#         a = []
#
#         for k in range(2):
#
#             a.append(int(input()))
#
#         matrix.append(a)
#
#     for i in range(2):
#
#         for j in range(2):
#             print(matrix[i][j], end=" ")

a = 2.45345
b = 2.45345
# print("%.2f"%a + "%.3f"%a)
print("%.2f %.2f"%(a,b))