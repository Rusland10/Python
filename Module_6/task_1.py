list = [i for i in input().split()]

for a in list:
    if int(a) % 2 == 0:
        list.remove(a)

print(" ".join(list))