testcase = int(input())
x_list = []
y_list = []
z_list = []
sum_x = 0
sum_y = 0
sum_z = 0

for i in range(testcase):
    x,y,z = list(map(int, input().split()))
    x_list.append(x)
    y_list.append(y)
    z_list.append(z)

for i in x_list:
    sum_x += i
for i in y_list:
    sum_y += i
for i in z_list:
    sum_z += i

if sum_x == 0 and sum_y==0 and sum_z== 0:
    print("YES")
else:
    print("NO")

