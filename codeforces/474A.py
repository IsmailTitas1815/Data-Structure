test_str = 'luckisbig'

print("The original string is : " + test_str)

# r_rot = 5
#
# l_rot = 2

shift = int(input())

res = (test_str * 3)[len(test_str) + shift:
                     2 * len(test_str) + shift]

print("The string after rotation is : " + str(res))

a = "luckisbigluckisbigluckisbig"