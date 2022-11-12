a = input()
left_a = a[len(a) // 2 + len(a) % 2:]
right_a = a[: len(a) // 2 + len(a) % 2]
print(left_a + right_a)