list = [i for i in input().split()]
list_ans = []
for a in range(0, len(list) - 1):
    if int(list[a]) < int(list[a + 1]):
        list_ans.append(list[a + 1])
print(" ".join(list_ans))