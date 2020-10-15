from math import ceil

n,m,a = list(map(int,input().split()))
print(ceil(n/a)*ceil(m/a))

# dhori n = 6 ar a =4, tahole n er dike puron korte 2(ceil) ta (a) lagbe,
# ar m = 9 dhori. tahole m er dike puron korte ceil(m/a) lagbe.
# ar ei 2 ta jinish gun korle amr total minimum tile lagbe ta bola jabe.