n,t = list(map(int,input().split()))
max = 0
min = 0
r = n%t
# print(r)
if r==0:
    part_for_min = n/t
    part_for_max = n-(t-1)
    # print(n,t)
    max = (part_for_max*(part_for_max-1))//2
    min = ((part_for_min*(part_for_min-1))//2) * t
    print(int(min),int(max))
else:
    #max
    part_for_max = n-(t-1)
    max = (part_for_max*(part_for_max-1))//2

    #min
    parti_per_team = n//t
    first_vag = t - r
    second_vag = r
    first_vag_sum = (parti_per_team*(parti_per_team-1)//2) * first_vag
    second_vag_sum = ((parti_per_team*(parti_per_team+1))//2) * second_vag
    min = first_vag_sum + second_vag_sum
    print(int(min),int(max))
# n = 1000000000 - (1000000-1)
# print((n*(n-1))//2)