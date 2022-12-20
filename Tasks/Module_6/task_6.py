list_1 = [i for i in input().split()]
list_2 = [i for i in input().split()]
list_ans = []
for a in range(0, len(list_1)):
    for b in range(0, len(list_2)):
        if list_1[a] == (list_2[b]):
            list_ans.append(list_1[a])
print(" ".join(list_ans))