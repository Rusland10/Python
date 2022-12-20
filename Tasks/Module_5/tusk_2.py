a = int(input())
N = 0
while 2 ** (N + 1) <= a:
    N += 1
print(N, 2 ** N)