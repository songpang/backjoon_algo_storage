N = int(input())
n = 0

if N>=1 and N<=100:
    while 0<N+1:
        print(" "*n + "*"*N)
        N -= 1
        n += 1