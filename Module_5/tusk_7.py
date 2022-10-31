a1 = 1
a2 = 1
n = input()
n = int(n)
i = 0
while i < n - 2:
    a_sum = a1 + a2
    a1 = a2
    a2 = a_sum
    i = i + 1
print(a2)