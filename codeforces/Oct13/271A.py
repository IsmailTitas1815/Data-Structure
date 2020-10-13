st = input()
while True:
    i = int(st) + 1
    st = str(i)
    li = {i for i in st}
    if len(li)==len(st):
        print(st)
        break
