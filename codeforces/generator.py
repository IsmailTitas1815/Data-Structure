def gen(x,y):
    while (x<y):
        yield x
        x+=1

for i in gen(1,6): print(i)
