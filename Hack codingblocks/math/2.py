n = int(input())

f = True
for i in range(2,n):
    if n%i==0:
        f = False
        break

if f == True:
    print("Prime")
else:
    print("Not Prime")