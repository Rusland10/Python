list = [i for i in input().split()]
max_number = -100000
min_number = 100000
max_index = 0
min_index = 0
for a in range(0, len(list)):
    if int(list[a]) > int(max_number):
        max_number = list[aber]
        max_index = a
    if int(list[a]) < int(min_number):
        min_number = list[a]
        min_index = a
list[max_index] = min_number
list[min_index] = max_number
print(" ".join(list))