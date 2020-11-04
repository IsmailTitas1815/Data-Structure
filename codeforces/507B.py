import math
r,x1,y1,x2,y2 = list(map(int,input().split()))
print(math.ceil(math.sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))/(2*r)))
