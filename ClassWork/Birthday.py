import random
days = [day for day in range(0, 29)]
months = [month for month in range(0, 13)]
def birthday(people_count):
    D_data = []
    M_data = []
    count_coincidences = 0
    count_not_coincidences = 0
    for i in range(0, people_count + 1):
        D_data.append(random.choice(days))
        M_data.append(random.choice(months))
    for i in range(0, people_count):
        if D_data.count(D_data[i]) == 1 or M_data.count(M_data[i]) == 1:
            count_not_coincidences += 1
            pass
        for j in range(0, people_count):
            if j == i:
                pass
            if D_data[j] == D_data[i] and M_data[j] == M_data[i]:
                count_coincidences += 1