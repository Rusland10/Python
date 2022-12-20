import random

__all__ = ['birthday']
def birthday(iteration, people_counter = 23 ):
    count = 0
    for i in range(iteration):
        age_list = []
        for j in range(people_counter):
            age = random.randint(1, 365)
            if age in age_list:
                count = count + 1
                break
            age_list.append(age)
    return "Вероятность совпадения ДР: " + str(count/(iteration/100)) + " %"


if __name__ == "__main__":
    print(birthday(15000, 23))