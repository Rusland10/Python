list = [i for i in input().split()]
list_ans = []
for a in range(0, len(list) - 1):
    if not list_ans.__contains__(list[a]) and not list_ans.__contains__(list[a + 1]):
        list_ans.append(list[a + 1])
        list_ans.append(list[a])
if len(list) % 2 != 0:
    list_ans.append(list[len(list) - 1])
print(" ".join(list_ans))