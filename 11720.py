a = int(input())
b = int(input())
base = 0

for i in range(1, a+1):
    base += b%(10)
    b //= 10

print(base)