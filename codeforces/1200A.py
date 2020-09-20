testcase = int(input())
LR = []
for i in range(10):
    LR.insert(i,0)

str = input().upper()
for i in range(testcase):
    if str[i] == "L":
        for j in range(0,10):
            if LR[j] == 0:
                LR[j] = 1
                break
    elif str[i] == "R":
        for k in range(9,-1,-1):
            if LR[k] == 0:
                LR[k] = 1
                break

    elif 0 <= int(str[i]) <= 9:
        LR[int(str[i])] = 0
for i in LR:
    print(i,end="")




#--------------------

#
# testcase = int(input())
# LR = []
# for i in range(10):
#     LR.insert(i,0)
#
# str = input().upper()
# for i in range(testcase):
#     if str[i] == "L":
#         for j in range(len(LR)):
#             if LR[j] == 0:
#                 LR[j] = 1
#                 break
#     elif str[i] == "R":
#         for k in reversed(range(len(LR))):
#             if LR[k] == 0:
#                 LR[k] = 1
#                 break
#     elif 0 <= int(str[i]) <= 9:
#         LR[int(str[i])] = 0
# for i in LR:
#     print(i,end="")