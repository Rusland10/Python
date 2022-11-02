list = [i for i in input().split()]
list_gen = []
for a in range(0, len(list)):
    if list_gen.__contains__(list[a]):
        print("ДА")
    else:
        print("НЕТ")
    list_gen.append(list[a])