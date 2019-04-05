N = int(input())

for i in range(1, 10):
    print(str(N)+" * ", end='')
    print(str(i)+" = "+str(i*N))


# 파이썬 1등 답안

# a = int(input())
# x = 1
# if a >= 1 and a <= 9:
#     while x < 10:
#         print("%d * %d = %d" %(a,x,a*x))
#         x += 1