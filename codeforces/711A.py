testcase = int(input())

for i in range(testcase):
    str = input()

    name = "titas"
    for s in name:
        if s.isalpha() and s == 't':
            name = name.replace("t", 'ok')
    print(name)