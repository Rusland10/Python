''' text = open("slova.txt.txt", encoding="utf-8")
text = text.read()
print(*text.title().split('\n'))
'''

import random
def slova() -> str:
    '''
    :return: Строка - рандомное слово из списка, которое надо угадать.
    '''
    with open(r'Practical-work №3/slova.txt.txt', encoding='UTF8') as sl:
        return random.choice(sl.read().splitlines()).lower()
def records() -> int:
    '''
    :return: максимальное количество очков за одну игровую сессию.
    '''
    with open(r'Practical-work №3/records.txt', mode='r', encoding='UTF8') as r:
        return int(r.read())
def writed(n: str):
    '''
    :param n: строка с числом максимальным количеством очков за одну игровую сессию.
    :return: -
    '''
    with open(r'Practical-work №3/records.txt', mode='w', encoding='UTF8') as r:
        r.write(n)
