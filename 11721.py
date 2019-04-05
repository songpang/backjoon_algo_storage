a = input()
d = len(a)
i = 0

while i != d:
    print(a[i], end='')
    i += 1
    if (i%10) == 0:
        print("\n", end='')


# a = input()
# for b in range (0, len(a), 10):
#     print(a[b:b+10])
# 블로그 우수 답안