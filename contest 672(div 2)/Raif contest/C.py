for i in range(int(input())):
    str = input()
    str = str.replace("AB","")
    print(str)
    str = str.replace("AB","")
    print(str)
    str = str.replace("BB","")
    print(str)
    if len(str)>0:
        print(len(str))
    else:
        print(0)
