a = int(input())
b = int(input())
count = 1
while a <= b:
    a += a / 10
    count += 1
print(count)